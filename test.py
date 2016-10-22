#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import webcitation


class CaptureTest(unittest.TestCase):

    def test_capture(self):
        archive_url = webcitation.capture("http://www.example.com/")
        self.assertTrue(archive_url.startswith("http://www.webcitation.org/"))


if __name__ == '__main__':
    unittest.main()
