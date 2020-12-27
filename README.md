> This repository has been archived because webcitation.org is no longer accepting archiving requests.

# webcitation

A simple Python wrapper for the [webcitation.org](http://www.webcitation.org/) capturing service.

[![PyPI version](https://badge.fury.io/py/webcitation.png)](http://badge.fury.io/py/webcitation)
[![Build Status](https://travis-ci.org/pastpages/webcitation.svg?branch=master)](https://travis-ci.org/pastpages/webcitation)
[![Coverage Status](https://coveralls.io/repos/github/pastpages/webcitation/badge.svg?branch=master)](https://coveralls.io/github/pastpages/webcitation?branch=master)

### Installation

```bash
$ pip install webcitation
```

### Python Usage

Import it.

```python
>>> import webcitation
```

Capture a URL.

```python
>>> archive_url = webcitation.capture("http://www.example.com/")
```

See where it's stored.

```python
>>> print archive_url
http://www.webcitation.org/6lSLkrUdV
```

### Command-line usage

The Python library is also installed as a command-line interface. You can run it from your terminal like so:

```bash
$ webcitation http://www.example.com/
```

The command has the same options as the Python API, which you can learn about from its help output.

```bash
$ archiveis --help
Usage: webcitation [OPTIONS] URL

  Archives the provided URL using the webcitation.org capturing service.

Options:
  -ua, --user-agent TEXT  User-Agent header for the web request
  --help                  Show this message and exit.
```
