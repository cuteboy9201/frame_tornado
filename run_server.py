#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author: YouShumin
@Date: 2020-06-08 11:16:24
@LastEditTime: 2020-06-10 10:55:17
@LastEditors: YouShumin
@Description: 
@FilePath: /frame_tornado/run_server.py
'''
import os
import sys

import tornado.options
from tornado.options import define, options
from configs.setting import PROJECT_NAME
import logging

LOG = logging.getLogger(__name__)
try:
    import sentry_sdk
    from sentry_sdk.integrations.tornado import TornadoIntegration

    sentry_sdk.init(
        dsn="https://b1696404710445e79550eb272ab9b5c1@sentry.io/1818061",
        integrations=[TornadoIntegration()])
except Exception as e:
    print(e)


class AppMain:
    def __init__(self):
        PATH_APP_ROOT = os.path.abspath(
            os.path.join(os.path.abspath(os.path.dirname(__file__))))
        if PATH_APP_ROOT not in sys.path:
            sys.path.insert(0, PATH_APP_ROOT)
        define("APP_PATH", default=PATH_APP_ROOT, help="app run dir")
        from app import web_app

        self._web_app = web_app()

    def start(self):
        return self._web_app.run()

    def stop(self):
        return self._web_app.stop()


if __name__ == "__main__":
    main = AppMain()
    try:
        main.start()
    except KeyboardInterrupt:
        main.stop()
