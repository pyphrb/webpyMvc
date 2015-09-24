#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'

'''
web.py route config

        self.urlConfig = (
            "/.*", "hello"

            )

'''

class Route(object):

    def __init__(self):
        self.urlConfig = None

    def url(self):
        self.urlConfig = (
            "/.*", "hello"
            )
        return self.urlConfig

