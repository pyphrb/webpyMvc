#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'
from app.config import Route
from app.config import Application
from app.control import hello
url = Route().url()
app = Application(url, globals()).application()


if __name__ == "__main__":
    app.run()
