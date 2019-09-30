#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/29

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class UserEditForm(FlaskForm):
    username = StringField(
        label='用户名',
        validators=[
            DataRequired("必须输入管理员名称"),
            Length(2, 20)
        ],
        description='管理员名称',
        render_kw={
            "type": "text",
            "autocomplete": "off",
            "placeholder": "用户名",
            "class": "form-control"
        }
    )
    phone = StringField(
        label='电话',
        validators=[
            DataRequired()
        ],
        description='电话号码',
        render_kw={
            "type": "tel",
            "autocomplete": "off",
            "placeholder": "电话",
            "class": "form-control"
        }
    )
    newpassword = PasswordField(
        label='新密码',
        render_kw={
            "autocomplete": "new-password",
            "placeholder": "新密码",
            "class": "form-control"
        }
    )
    newpassword2 = PasswordField(
        label='确认密码',
        validators=[
            EqualTo("newpassword", message="两次密码不一致")
        ],
        render_kw={
            "autocomplete": "new-password",
            "placeholder": "确认密码",
            "class": "form-control"
        }
    )
    submit = SubmitField(
        label='确认修改',
        render_kw={
            "class": "btn btn-success"
        }
    )
