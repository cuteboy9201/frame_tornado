#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author: YouShumin
@Date: 2020-06-10 12:02:00
@LastEditTime: 2020-06-10 14:15:32
@LastEditors: YouShumin
@Description: Another flat day
@FilePath: /frame_tornado/configs/req_info.py
'''

CORE_SERVER_INFO = dict(domain="192.168.2.39",
                        port=40000,
                        protocol_type="http",
                        GET_TEST_DATA=dict(method="GET",
                                           uri_pattern="/test",
                                           help="get请求放回请求参数"),
                        POST_TEST_DATA=dict(method="POST",
                                            uri_pattern="/test",
                                            help="post请求返回请求参数"))
