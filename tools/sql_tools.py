#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:05:10 2021

@author: LiShuang
"""


import sqlite3

def execute_sql(statement, db='yelp_fusion_cache.db'):
    db = sqlite3.connect(db)
    c = db.cursor()
    c.execute(statement)
    if statement.startswith('SELECT'):
        data = c.fetchall()
        db.commit()
        db.close()
        return data
    else:
        db.commit()
        db.close()
    
def select_statement(table_name, business_id):
    statement = "SELECT * FROM {} WHERE Business_id='{}'".format(table_name, business_id)
    return statement

def insert_statement(table_name, values):
    statement = 'INSERT INTO %s ' % table_name + 'VALUES (' + ','.join(repr(value) for value in values) + ')'
    return statement
