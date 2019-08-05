#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-3 
# @Author  : JiaoJianglong


from .users import users
from .gene import gene

DEFAULT_BLUEPRINT = (
    (users,'/users'),
    (gene,'/gene'),
)


# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
