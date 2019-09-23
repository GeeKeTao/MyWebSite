#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/23
# 创建后台蓝图

from flask import Blueprint


admin = Blueprint('admin', __name__)

from app.admin.views.main import *
from app.admin.views.logs import *
