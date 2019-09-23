#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/4

# 项目运行入口文件

from app import app

if __name__ == '__main__':
    app.run('127.0.0.1', '8888', True)  # 运行地址为:127.0.0.1  端口为:8888  开启调试模式:True
