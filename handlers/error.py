#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author: YouShumin
@Date: 2020-06-10 10:57:29
@LastEditTime: 2020-06-10 11:14:07
@LastEditors: YouShumin
@Description: "设置默认404页面"
@FilePath: /frame_tornado/handlers/error.py
'''
from oslo.web.requesthandler import MixinRequestHandler
from oslo.web.route import route

import logging

LOG = logging.getLogger(__name__)


@route(r".*")
class ErrorHandler(MixinRequestHandler):
    def get(self):
        self.render("404.html")
        return

    def post(self):
        self.send_fail(msg="请联系管理员添加白名单...")
        return
