#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/24
# 数据库管理

import getpass

from app.config import SYS_INIT_DATA as sysData
from app import manager
from app.models import *
from werkzeug.security import generate_password_hash, check_password_hash


@manager.command
def initdb():
    """初始化数据表"""
    db.drop_all()
    db.create_all()
    u = Admin(name='geektadmin', password=generate_password_hash('geektadmin'), phone='17601478025', gender=True)
    db.session.add(u)
    db.session.commit()
    initsys()
    print("初始化数据库成功......")


@manager.command
def initsys():
    """初始化系统配置"""
    for s in sysData:
        sdata = SystemData(systemkey=s, systemval=sysData[s], admin_id=1, modifytime=datetime.utcnow())
        db.session.add(sdata)
    db.session.commit()
    print("初始化系统配置成功......")

@manager.command
def createsuperuser():
    """创建超级用户"""
    username = input('请输入超级用户名：')
    if Admin.query.filter_by(name=username).first():
        print('该超级用户已存在！')
    else:
        password = getpass.getpass('请输入超级用户密码：')
        password_hash = generate_password_hash(password)
        admin = Admin(name=username, password=password_hash, is_super=True)
        db.session.add(admin)
        db.session.commit()
        print('创建超级用户成功...')


# 运行数据库管理程序
if __name__ == '__main__':
    manager.run()
