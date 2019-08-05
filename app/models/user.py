#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-3 
# @Author  : JiaoJianglong

from flask_login import UserMixin
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    """用户类"""
    __tablename__='User'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),unique=True)
    password_hash = db.Column(db.String(256))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return self.username

    def verify_password(self, password):
        print(self.password_hash)
        print(generate_password_hash(password),"*"*80)
        return check_password_hash(self.password_hash, password)

    @property
    def password(self):
        raise AttributeError('密码不可读')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


