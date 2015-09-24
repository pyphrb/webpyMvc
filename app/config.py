#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'
import web

class Route(object):

    def __init__(self):
        self.urlConfig = None

    def url(self):
        self.urlConfig = (
            "/.*", "hello"

            )
        return self.urlConfig


class Application(object):

    def __init__(self, URLS, GLOBALS):
        self.urls = URLS
        self.globals = GLOBALS
        self.app = None

    def application(self):
        self.app = web.application(self.urls, self.globals)
        return self.app

class Dbconfig(object):

    def __init__(self):
        self.db = None