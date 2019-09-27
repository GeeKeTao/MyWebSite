#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/23

from flask import session, request, redirect, url_for, render_template
from app.admin import admin
from app.admin.utils import is_admin_login
from app import db


@admin.route('/')
@is_admin_login
def index():
    return render_template('admin/index.html')
