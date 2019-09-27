#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/23

from flask import session, flash, request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash
from app import db
from app.admin import admin
from app.admin.forms.logs import LoginForm
from app.admin.utils import is_admin_login
from app.models import Admin, AdminLog


# 登录
@admin.route('/login/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    print('开始登陆-验证：')
    print(form.validate_on_submit())
    if form.validate_on_submit():

        name = form.username.data
        password = form.password.data
        admin = Admin.query.filter_by(name=name).first()
        if admin and admin.verify_password(password):
            # 存储 session 信息
            session['admin_id'] = admin.id
            session['admin'] = admin.name
            remote_ip = request.remote_addr

            # 存储登录信息到登录日志
            adminlog = AdminLog(
                admin_name=admin.name,
                ip=remote_ip
            )
            db.session.add(adminlog)
            db.session.commit()
            print('管理员登录成功！')
            return redirect(url_for('admin.index'))
        else:
            flash('帐号或密码错误')
    print(form.errors)
    return render_template('admin/login.html', form=form)


# 登出
@admin.route('/logout/')
@is_admin_login
def logout():
    session.pop('admin_id', None)
    session.pop('admin', None)
    return redirect(url_for('admin.login'))
