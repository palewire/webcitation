#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import click
import random
import requests
from six.moves import range
from six.moves.urllib.parse import urljoin


def capture(
    target_url,
    user_agent="savepagenow (https://github.com/pastpages/savepagenow)"
):
    """
    Archives the provided URL using the webcitation.org capturing service.

    Returns the URL where the capture is stored.
    """
    # Put together the URL that will save our request
    domain = "http://www.webcitation.org"
    save_url = urljoin(domain, "/archive.php")

    # Send the capture request to webcitation.org
    headers = {
        'User-Agent': user_agent,
    }
    data = {
        "email": _get_random_email(),
        "url": target_url,
    }
    response = requests.post(save_url, headers=headers, data=data)

    # build the regular expression to find
    # the location of the archived resource
    archived_location_regex = re.compile(
        r"""(
           [A-Za-z]{4,5}:// # matches http(s)://
           [a-z]{3}\.       # matches www.
           [a-z]{11}        # matches webcitation
           \.[a-z]{3}/      # matches .org/
           [a-zA-z0-9]{9}   # matches 9 character
                            # archived resource
                            # unique identifier
           )                # end capture group
       """, re.X
    )

    # search through the returned html page for the location
    # to the archived resource
    # when found, the url-m is contained in group 0 of the returned MatchObject
    # see https://docs.python.org/3/library/re.html#re.regex.search
    archive_url = archived_location_regex.search(response.text).group(0)

    return archive_url


def _get_random_email():
    """
    Returns a random email address.
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"
    choices = alpha + "0123456789"
    domains = [".com", ".org", ".edu", ".co.uk", ".net"]
    text = []

    # build the user portion of the email
    for i in range(0, random.randint(2, 4)):
        # need 2-4 individual chunks with length between 1-3 characters
        for j in range(0, random.randint(1, 3)):
            text.append(choices[random.randint(0, len(choices) - 1)])

    text.append('@')

    # build the email host
    for i in range(0, random.randint(2, 3)):
        for j in range(0, random.randint(1, 3)):
            text.append(alpha[random.randint(0, len(alpha) - 1)])

    text.append(domains[random.randint(0, 4)])

    return ''.join(text)


@click.command()
@click.argument("url")
@click.option("-ua", "--user-agent", help="User-Agent header for the web request")
def cli(url, user_agent):
    """
    Archives the provided URL using archive.org's Wayback Machine.

    Raises a CachedPage exception if archive.org declines to conduct a new
    capture and returns a previous snapshot instead.
    """
    kwargs = {}
    if user_agent:
        kwargs['user_agent'] = user_agent
    archive_url = capture(url, **kwargs)
    click.echo(archive_url)


if __name__ == "__main__":
    cli()
