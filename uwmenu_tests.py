#!/usr/bin/env python

"""Test UW Menu Flask application."""

import unittest

from uwmenu import app, attach_filters

class UWMenuTestCase(unittest.TestCase):

    def setUp(self):
        attach_filters()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_menu_pageload(self):
        """Ensure description on menu page is present."""
        rv = self.app.get('/')
        assert 'Weekly menus for the University of Waterloo\'s on-campus eateries.' in rv.data

if __name__ == "__main__":
    unittest.main()
