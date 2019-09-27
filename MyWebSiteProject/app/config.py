#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/23
# 配置信息
import os


# 配置数据库
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root@localhost:3306/geekt"  # mysql://username:password@server/db
# SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 文件存放位置

BASEDIR = os.path.abspath(os.path.dirname(__file__))  # 获取当前项目所在目录的绝对路径
# 上传文件目录配置
UP_DIR = os.path.join(BASEDIR, "static/uploads/")
FC_DIR = os.path.join(BASEDIR, "static/uploads/users/")

# 分页配置
PER_PAGE = 5

# 配置阿里云OSS
# 初始化AccessKeyId、AccessKeySercret、Endpoint等信息
OSS_ACCESS_KEY_ID = 'LTAI4FjGMtFNSTY7ab4FGTCF'
OSS_ACCESS_KEY_SECRET = 'gMDznxZTSGQrMgkY62vgYvaARcTFly'
OSS_ENDPOINT = 'http://oss-cn-beijing.aliyuncs.com'
OSS_BUCKET_NAME = 'geekt-buket'
OSS_BUCKET_FOLDER = 'geektWebSite/'

# 初始系统参数配置
SYS_INIT_DATA = {
    'defAdmin': 'geektadmin',  # 初始管理员名称
    'defPwd': 'geektAdmin',  # 初始管理员密码
    'defAdminImg': BASEDIR + '/static/admin/images/admin.jpg',  # 初始管理员头像
    'defFilePath': UP_DIR,  # 默认服务器文件存放地址
    'filePath': 'files/',  # 文件存放地址
    'imgPath': 'images/',  # 图片存放地址
    'videoPath': 'videos/',  # 视频存放地址
    'imgType': '[jpg, png, jpeg, gif]',  # 图片上传限定格式
    'videpType': '[mp4, rmvb]',  # 视频上传限定格式
    'imgSize': '5120',  # 图片上传限定大小
    'videoSize': '102400',  # 视频上传限定大小
    'fileSize': '10240',  # 文件上传限定大小
    'ossAccessKeyId': OSS_ACCESS_KEY_ID,  # 阿里云OSS AccessKeyId
    'ossAccessKeySecret': OSS_ACCESS_KEY_SECRET,  # 阿里云OSS AccessKeySecret
    'ossEndpoint': OSS_ENDPOINT,  # 阿里云OSS Endpoint
    'ossBucketName': OSS_BUCKET_NAME,  # 阿里云OSS BucketName
    'ossBucketFolder': OSS_BUCKET_FOLDER  # 阿里云对象存储文件存放目录
}
