#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-3 
# @Author  : JiaoJianglong

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# 定义配置基类
class Config:
    # 秘钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'

    # 数据库公用配置
    # 无警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 额外的初始化操作
    @staticmethod
    def init_app(app):
        pass


# 开发环境配置
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://jiao1:jiao123456@192.168.0.102/anzhi'

    MONGO_URI = "mongodb://{username}:{password}@{server}:{port}/{database}". \
        format(username="jiao", password="jiao123456", server="127.0.0.1",
               port=8975, database="anzhi")


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://jiao1:jiao123456@192.168.0.102/anzhi'

    MONGO_URI = "mongodb://{username}:{password}@{server}:{port}/{database}". \
        format(username="jiao", password="jiao123456", server="127.0.0.1",
               port=8975, database="anzhi")

# 生成一个字典，用来根据字符串找到对应的配置类。
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

