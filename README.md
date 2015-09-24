<div style="font-family: 'Lucida Grande', 'Segoe UI', 'Apple SD Gothic Neo', 'Malgun Gothic', 'Lucida Sans Unicode', Helvetica, Arial, sans-serif; font-size: 0.9em; overflow-x: hidden; overflow-y: auto; margin: 0px !important; padding: 5px 20px 26px !important; background-color: rgb(255, 255, 255);font-family: 'Hiragino Sans GB', 'Microsoft YaHei', STHeiti, SimSun, 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', 'Segoe UI', AppleSDGothicNeo-Medium, 'Malgun Gothic', Verdana, Tahoma, sans-serif; padding: 20px;padding: 20px; color: rgb(34, 34, 34); font-size: 15px; font-family: 'Roboto Condensed', Tauri, 'Hiragino Sans GB', 'Microsoft YaHei', STHeiti, SimSun, 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', 'Segoe UI', AppleSDGothicNeo-Medium, 'Malgun Gothic', Verdana, Tahoma, sans-serif; line-height: 1.6; -webkit-font-smoothing: antialiased; background: rgb(255, 255, 255);"><h2 id="webpymvc一个基于web.py的mvc简洁框架" style="clear: both;font-size: 1.8em; font-weight: bold; margin: 1.275em 0px 0.85em;margin-top: 0px;border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(230, 230, 230);"><a name="webpymvc一个基于web.py的mvc简洁框架" href="#webpymvc一个基于web.py的mvc简洁框架" style="text-decoration: none; vertical-align: baseline;color: rgb(50, 105, 160);"></a>webpyMVC一个基于web.py的MVC简洁框架</h2><h3 id="manager.py" style="clear: both;font-size: 1.6em; font-weight: bold; margin: 1.125em 0px 0.75em;"><a name="manager.py" href="#manager.py" style="text-decoration: none; vertical-align: baseline;color: rgb(50, 105, 160);"></a>Manager.py</h3><pre style="border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px; word-wrap: break-word; border: 1px solid rgb(204, 204, 204); overflow: auto; padding: 0.5em;"><code data-origin="<pre><code>#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'
from app.config import Route
from app.config import Application#Application配置
from app.control import hello#调用方法
url = Route().url()#在app文件夹里面的config中的Route类中类中配置url
app = Application(url, globals()).application()


if __name__ == &quot;__main__&quot;:
    app.run()
</code></pre>" style="border: 0px; display: block;font-family: Consolas, Inconsolata, Courier, monospace; font-weight: bold; white-space: pre; margin: 0px;border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px; word-wrap: break-word; border: 1px solid rgb(204, 204, 204); padding: 0px 5px; margin: 0px 2px;font-size: 1em; letter-spacing: -1px; font-weight: bold;">#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'
from app.config import Route
from app.config import Application#Application配置
from app.control import hello#调用方法
url = Route().url()#在app文件夹里面的config中的Route类中类中配置url
app = Application(url, globals()).application()


if __name__ == "__main__":
    app.run()
</code></pre><h3 id="config.py" style="clear: both;font-size: 1.6em; font-weight: bold; margin: 1.125em 0px 0.75em;"><a name="config.py" href="#config.py" style="text-decoration: none; vertical-align: baseline;color: rgb(50, 105, 160);"></a>config.py</h3><pre style="border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px; word-wrap: break-word; border: 1px solid rgb(204, 204, 204); overflow: auto; padding: 0.5em;"><code data-origin="<pre><code>#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'
import web

class Route(object):

    def __init__(self):
        self.urlConfig = None

    def url(self):
        self.urlConfig = (
            &quot;/.*&quot;, &quot;hello&quot;

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
</code></pre>" style="border: 0px; display: block;font-family: Consolas, Inconsolata, Courier, monospace; font-weight: bold; white-space: pre; margin: 0px;border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px; word-wrap: break-word; border: 1px solid rgb(204, 204, 204); padding: 0px 5px; margin: 0px 2px;font-size: 1em; letter-spacing: -1px; font-weight: bold;">#!/usr/bin/env python
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
</code></pre><h3 id="control.py" style="clear: both;font-size: 1.6em; font-weight: bold; margin: 1.125em 0px 0.75em;"><a name="control.py" href="#control.py" style="text-decoration: none; vertical-align: baseline;color: rgb(50, 105, 160);"></a>control.py</h3><pre style="border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px; word-wrap: break-word; border: 1px solid rgb(204, 204, 204); overflow: auto; padding: 0.5em;"><code data-origin="<pre><code>


class hello:
    def GET(self):
        return &quot;hello world&quot;
</code></pre>" style="border: 0px; display: block;font-family: Consolas, Inconsolata, Courier, monospace; font-weight: bold; white-space: pre; margin: 0px;border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px; word-wrap: break-word; border: 1px solid rgb(204, 204, 204); padding: 0px 5px; margin: 0px 2px;font-size: 1em; letter-spacing: -1px; font-weight: bold;">


class hello:
    def GET(self):
        return "hello world"
</code></pre></div>
