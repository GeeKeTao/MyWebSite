#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/4

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager  # 命令行操作数据库
from flask_migrate import Migrate  # 数据库迁移
from flask_moment import Moment  # 解决时间问题
import pymysql
pymysql.install_as_MySQLdb()  # 解决数据库报错

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(db, app)
moment = Moment(app)


# 导入蓝图
from app.admin import admin as admin_blueprint
from app.home import home as home_blueprint

# 注册 admin 蓝图 url_prefix = '/admin'(添加后台管理前缀 /admin)
app.register_blueprint(admin_blueprint, url_prefix='/admin')
# 注册 home 蓝图
app.register_blueprint(home_blueprint)
