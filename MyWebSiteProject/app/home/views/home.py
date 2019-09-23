#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/23

from app.home import home


@home.route('/')
def index():
    return 'Hello Wellcom To GeektWebSite !'
