#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/26
# 阿里云存储 OSS 功能

import os
import datetime
import oss2
import app.config as config


class Oss:

    # 初始化AccessKeyId、AccessKeySercret、Endpoint信息
    def __init__(self):
        self.__accessKeyId = config.OSS_ACCESS_KEY_ID
        self.__accessKeySecret = config.OSS_ACCESS_KEY_SECRET
        self.__auth = oss2.Auth(self.__accessKeyId, self.__accessKeySecret)
        self.__bucket = oss2.Bucket(self.__auth, config.OSS_ENDPOINT, config.OSS_BUCKET_NAME)
        self.__bucket_folder = config.OSS_BUCKET_FOLDER

    # 上传对象 字符串('123')、Bytes(b'hello')、Unicode(u'world')、本地文件(必须以二进制的方式打开文件再进行上传)、上传网络流
    def up_object(self, objname, obj):
        bucket = self.__bucket
        result = bucket.put_object(self.__bucket_folder + objname, obj)
        print('Http Status: {0}'.format(result.status))
        print('Request Id: {0}'.format(result.request_id))
        print('Etag: {0}'.format(result.etag))
        print('Date: {0}'.format(result.headers['date']))
        return result

    # 上传文件
    def up_files(self):
        pass


testObj = Oss()
test = testObj.up_object('text5.txt', 'hello geekt')

print('test: ', test)
