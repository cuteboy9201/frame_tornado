#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Youshumin
@Date: 2019-08-21 11:13:46
@LastEditors: YouShumin
@LastEditTime: 2020-06-08 16:35:12
'''
import logging
import logging.config
import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from configs.setting import (ALLOW_HOST, COOKIE_SECRET, HOST, LOGFILE, PORT,
                             PROJECT_NAME, RUN_NUM_CORE)
from handlers import *
from oslo.web.route import route
from tornado.log import enable_pretty_logging
from tornado.options import define, options
from oslo.utils.log import LogHandler
debug = os.environ.get("RUN_ENV")

LOG = logging.getLogger(__name__)


class RouteHandler(object):
    """注册路由"""
    def __init__(self):
        """
        需要配置这里实现注册路由...
            自动注册路由的方式可以继承 application实现
            我这边是想实现像flask蓝本一样实现注册...所以暂时设置为这样
        """
        self.route = route
        super(RouteHandler, self).__init__()


class Application(tornado.web.Application, RouteHandler):
    """初始化application"""
    def __init__(self):
        configs = dict(
            debug=options.debug,
            cookie_secret=COOKIE_SECRET,
            autoescape=None,
        )
        RouteHandler.__init__(self)
        tornado.web.Application.__init__(self, self.route.get_urls(),
                                         **configs)


class WebApp():
    """应用启动唯一入口"""
    def __init__(self):
        """
            初始化启动信息
                运行环境 debug
                运行ip host
                启动端口 port
        """
        if debug != "prod":
            define("debug", default=True, help="enable debug mode")
            define("allow_host", default=[], help="allow host")
        else:
            define("debug", default=False, help="enable debug mode")
            define("allow_host", default=ALLOW_HOST, help="allow host")
        define("host", default=HOST, help="run on this host", type=str)
        define("port", default=PORT, help="run on this port", type=int)

    def run(self):
        LogHandler(LOGFILE)
        http_server = tornado.httpserver.HTTPServer(Application(),
                                                    xheaders=True)
        if options.debug:
            options.log_to_stderr = True
            enable_pretty_logging()
            logging.getLogger().setLevel(logging.DEBUG)
            http_server.listen(options.port, address=options.host)
            LOG.info("start app [%s] for %s:%s", PROJECT_NAME, options.host,
                     options.port)
        else:
            enable_pretty_logging()
            http_server.bind(options.port, address=options.host)
            http_server.start(RUN_NUM_CORE)
        try:
            tornado.ioloop.IOLoop.instance().start()
        except KeyboardInterrupt:
            tornado.ioloop.IOLoop.instance().stop()

    def stop(self):
        tornado.ioloop.IOLoop.instance().stop()


def web_app():
    return WebApp()
