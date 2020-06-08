#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author: YouShumin
@Date: 2020-06-08 11:16:24
@LastEditTime: 2020-06-08 16:35:05
@LastEditors: YouShumin
@Description: Another flat day
@FilePath: /frame_tornado/configs/setting.py
'''

import os

debug = os.environ.get("RUN_ENV")

if debug == "prod":
    from configs.cfg import PORT, LOGDIR, ALLOW_HOST
else:
    from configs.dev_cfg import PORT, LOGDIR, ALLOW_HOST

PATH_APP_ROOT = os.path.abspath(
    os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))))

COOKIE_SECRET = "0wEE^@!TKGwbC0efdgDgmHC48HT620YJl^zE6qE"
PROJECT_NAME = "frame_tornado"
HOST = "0.0.0.0"
LOGFILE = LOGDIR + PROJECT_NAME + ".log"
RUN_NUM_CORE = 4
