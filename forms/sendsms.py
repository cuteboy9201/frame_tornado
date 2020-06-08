#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author: YouShumin
@Date: 2019-12-26 14:53:42
@LastEditTime: 2020-06-01 16:16:06
@LastEditors: YouShumin
@Description: 
@FilePath: /KwSendSms/forms/sendsms.py
'''
import logging

from oslo.form.fields import BoolField, EmailField, IntegerField, StringField, StringListField
from oslo.form.form import Form


class SendSmsPostForm(Form):
    def __init__(self, handler=None):
        self.phonenumber = IntegerField(required=True)
        self.typecode = StringField(required=True)
        self.reqaddress = StringField(required=False)
        # self.sendparam = IntegerField(required=False)
        super(SendSmsPostForm, self).__init__(handler=handler)


class CheckSmsCodeGetForm(Form):
    def __init__(self, handler=None):
        self.phonenumber = IntegerField(required=True)
        self.typecode = StringField(required=True)
        self.smscode = IntegerField(required=True)
        super(CheckSmsCodeGetForm, self).__init__(handler=handler)
