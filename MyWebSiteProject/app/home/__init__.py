#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/23
# 创建前台蓝图

from flask import Blueprint


home = Blueprint('home', __name__)

from app.home.views.home import *