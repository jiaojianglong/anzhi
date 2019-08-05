#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-4 
# @Author  : JiaoJianglong

from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


from app.models.user import User


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='请填写用户名'), Length(4, 20, message='长度在4到20个字符之间')])
    password = PasswordField('密码', validators=[DataRequired(message='请填写密码'), Length(8, 20, message='密码长度在8到20之间'),
                                               EqualTo('confirm', message='密码不一致')])
    confirm = PasswordField('密码确认')
    submit = SubmitField('注册')

    # 检验username是否存在
    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('用户名已存在')


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='用户名不能为空')])
    password = PasswordField('密码', validators=[DataRequired(message='密码不能为空')])
    remember = BooleanField('记住我', default=True)
    submit = SubmitField('登录')