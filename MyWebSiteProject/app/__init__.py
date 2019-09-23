#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/4

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate
from flask_moment import Moment
from app.admin import admin as admin_blueprint
from app.home import home as home_blueprint
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# 注册 admin 蓝图 url_prefix = '/admin'(添加后台管理前缀 /admin)
app.register_blueprint(admin_blueprint, url_prefix='/admin')
# 注册 home 蓝图
app.register_blueprint(home_blueprint)
