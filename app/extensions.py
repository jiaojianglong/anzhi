#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-3 
# @Author  : JiaoJianglong

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo

# 创建对象
db = SQLAlchemy()
migrate = Migrate(db=db)
login_manager = LoginManager()
bootstrap = Bootstrap()
mongo = PyMongo()


# 初始化
def config_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mongo.init_app(app)

    # 指定登录的端点
    login_manager.login_view = 'users.login'
    # 需要登录时的提示信息
    login_manager.login_message = '需要先登录'
    login_manager.session_protection = 'strong'