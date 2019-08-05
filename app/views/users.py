#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-3 
# @Author  : JiaoJianglong


from flask import Blueprint, redirect, render_template, flash, url_for, request
from flask_login import login_required, login_user, logout_user

from app.models.user import User
from app.extensions import login_manager, db
from app.forms.user import RegisterForm, LoginForm

users = Blueprint('users', __name__)


@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)


@users.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


@users.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter(User.username == username).first()
        if not user:
            flash('用户名或密码错误')
        elif not user.verify_password(form.password.data):
            flash('用户名或密码错误')
        else:
            login_user(user, remember=form.remember.data)
            flash('登录成功')
            return redirect(url_for('gene.message', next=request.args.get('next')))
    return render_template('login.html', form=form)


@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))