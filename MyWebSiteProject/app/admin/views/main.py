#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/23

from flask import session, request, redirect, url_for, render_template
from app.admin import admin


@admin.route('/')
def index():
    return 'Hello Wellcom To GeektAdmin !'
