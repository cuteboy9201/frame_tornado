#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author: YouShumin
@Date: 2020-06-08 11:16:24
@LastEditTime: 2020-06-08 16:16:54
@LastEditors: YouShumin
@Description: ""
@FilePath: /frame_tornado/handlers/test.py
'''
from oslo.web.requesthandler import MixinRequestHandler
from oslo.web.route import route
from tornado.gen import coroutine
from tornado.web import asynchronous

import logging

LOG = logging.getLogger(__name__)


@route('/test')
class TestHandler(MixinRequestHandler):
    @asynchronous
    @coroutine
    def get(self):
        req_data = self.request_body()

        self.send_ok(data=req_data)
        return

    @asynchronous
    @coroutine
    def post(self):
        req_data = self.request_body()
        self.send_ok(data=req_data)
        return
