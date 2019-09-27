#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/23
from functools import wraps
from flask import session, flash, redirect, url_for, request, abort
from app import db
from app.models import AdminOperationLog, Admin, Auth


def is_admin_login(f):
    """判断是否登录"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        if session.get('admin', None):
            return f(*args, **kwargs)
        else:
            flash("管理员请登录 %s" % f.__name__)
            return redirect(url_for('admin.login'))
    return wrapper


def write_adminlog(content):
    """向数据库中写入管理员操作日志"""
    adminOperationLog = AdminOperationLog(
        admin_id=session.get('admin_id'),
        content=content,
        ip=request.remote_addr
    )
    db.session.add(adminOperationLog)
    db.session.commit()

