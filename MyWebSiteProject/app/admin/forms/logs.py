#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/24
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp
from flask_wtf.file import FileAllowed


class BaseForm(FlaskForm):
    username = StringField(
        label='管理员',
        validators=[
            DataRequired("必须输入管理员名称"),
            Length(2, 20)
        ],
        description='管理员名称',
        render_kw={
            "placeholder": "请输入管理员...",
            "class": "form-control"
        }
    )
    password = PasswordField(
        label='密码',
        validators=[
            DataRequired()
        ],
        render_kw={
            "placeholder": "请输入密码...",
            "class": "form-control"
        }
    )


class LoginForm(BaseForm):
    submit = SubmitField(
        label='登录',
        render_kw={
            "class": "btn btn-success btn-flat m-b-30 m-t-30"
        }
    )
