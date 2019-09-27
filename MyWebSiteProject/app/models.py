#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/23

from datetime import datetime
from app import db

# 表前缀
table_prefix = 'geekt_'


# 管理员数据表
class Admin(db.Model):
    __tablename__ = table_prefix + 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键id
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 添加的时间
    userid = db.Column(db.Integer, unique=True, index=True)  # id---不能重复、添加索引
    name = db.Column(db.String(40), unique=True, index=True)  # 名称---不能重复、添加索引
    password = db.Column(db.String(300))  # 密码
    phone = db.Column(db.String(20), unique=True)  # 电话---不能重复
    gender = db.Column(db.Boolean)  # 用户性别 1---男 0---女
    img_url = db.Column(db.String(300))  # 用户头像
    is_super = db.Column(db.Boolean, default=False)

    # 关联其他表
    roleid = db.Column(db.Integer, db.ForeignKey(table_prefix + 'role.id'))  # 角色管理
    adminlogs = db.relationship("AdminLog", backref='admin')  # 管理员登录日志
    adminoperationlogs = db.relationship("AdminOperationLog", backref="admin")  # 管理员操作日志

    def verify_password(self, password):
        from werkzeug.security import check_password_hash
        # 判断密码是否正确
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<Admin %s>" % self.name


# 管理员登录日志
class AdminLog(db.Model):
    __tablename__ = table_prefix + 'admin_log'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    ip = db.Column(db.String(30))  # 登录IP
    area = db.Column(db.String(50))  # 登录所在位置

    # 关联管理员数据表
    admin_name = db.Column(db.String(40), db.ForeignKey(Admin.name))  # 管理员登录日志与管理员之间的关联


    def __repr__(self):
        return "<AdminLog %s>" % self.ip


# 管理员操作日志
class AdminOperationLog(db.Model):
    __tablename__ = table_prefix + 'admin_operation_log'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    content = db.Column(db.String(80))  # 操作内容
    ip = db.Column(db.String(30))  # 登录IP
    area = db.Column(db.String(50))  # 登录所在位置

    # 关联管理员数据表
    admin_id = db.Column(db.Integer, db.ForeignKey(Admin.id))  # 管理员操作日志与管理员之间的关联

    def __repr__(self):
        return "<AdminOperationLog %s>" % self.ip


# 角色管理
class Role(db.Model):
    __tablename__ = table_prefix + 'role'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    name = db.Column(db.String(20), unique=True)  # 角色名称--不能重复

    # 管理其他表
    auths = db.Column(db.String(100))
    admins = db.relationship('Admin', backref='role')

    def __repr__(self):
        return "<Role %s>" % self.name


# 权限管理数据表
class Auth(db.Model):
    __tablename__ = table_prefix + 'auth'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    name = db.Column(db.String(20), unique=True)  # 权限名称---不能重复
    url = db.Column(db.String(50), unique=True)  # 权限URL地址

    def __repr__(self):
        return "<Auth %s>" % self.name


# 系统参数数据表
class SystemData(db.Model):
    __tablename__ = table_prefix + 'system_data'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    systemkey = db.Column(db.String(100), unique=True)  # 参数名---不能重复
    systemval = db.Column(db.String(300))  # 参数值
    modifytime = db.Column(db.DateTime, default=datetime.utcnow())  # 修改时间
    # 关联管理员数据表
    admin_id = db.Column(db.Integer, db.ForeignKey(Admin.id))  # 系统参数修改与管理员之间的关联

    def __repr__(self):
        return "<SystemData %s>" % self.systemkey
