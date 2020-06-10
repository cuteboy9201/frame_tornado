#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author: YouShumin
@Date: 2020-06-10 11:54:37
@LastEditTime: 2020-06-10 14:16:16
@LastEditors: YouShumin
@Description: Another flat day
@FilePath: /frame_tornado/utils/rest_test.py
'''

from oslo.web.httpclient import Request as httpclient
from configs.req_info import CORE_SERVER_INFO


class CoreServerRequest(httpclient):
    def __init__(self):
        httpclient.__init__(self)
        self.set_port(CORE_SERVER_INFO.get("port"))
        self.set_domain(CORE_SERVER_INFO.get("domain"))
        self.set_protocol_type(CORE_SERVER_INFO.get("protocol_type"))
        self.set_request_read_timeout(2)
        self.set_request_connect_timeout(2)

    def GameInfoGet(self):
        req_info = CORE_SERVER_INFO.get("GET_TEST_DATA")
        self.set_uri_pattern(req_info.get("uri_pattern"))
        self.set_method(req_info.get("method"))


if __name__ == "__main__":
    rq = CoreServerRequest()
    rq.GameInfoGet()
    rq.add_body_params("nihap", "我是睡")
    rq.add_body_params("zcadfa", "xxx")
    req = rq.fetch()
    code, head, content = req.get_response_object()
    import json
    print(json.loads(content))
