__author__ = 'pyphrb'
import web

class Application(object):

    def __init__(self, URLS, GLOBALS):
        self.urls = URLS
        self.globals = GLOBALS
        self.app = None

    def application(self):
        self.app = web.application(self.urls, self.globals)
        return self.app