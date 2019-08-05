#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-5 
# @Author  : JiaoJianglong

from app.extensions import mongo


class Transcripts():

    def __init__(self):
        self.conn = mongo.db.transcripts

    def insert(self, vals):

        self.conn.insert_many(vals)