#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-3 
# @Author  : JiaoJianglong

import os

from flask_script import Manager
from flask_migrate import MigrateCommand

from app import create_app


# 从环境变量中获取config_name
config_name = os.environ.get('FLASK_CONFIG') or 'default'

# 生成app
app = create_app(config_name)

manager = Manager(app)

manager.add_command('db',MigrateCommand)


@manager.command
def create_all():
    from app.extensions import db
    db.create_all()


if __name__ == '__main__':
    manager.run()