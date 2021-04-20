#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:06:36 2021

@author: LiShuang
"""

def parse_business_details(info):
    if info.get('error'):
        return ''
    else:
        ID = info['id']
        name = info['name']
        is_closed = str(info['is_closed'])
        url = info['url']
        phone = info['phone']
        display_phone = info['display_phone']
        review_count = str(info['review_count'])
        category = '|'.join([alia['title'] for alia in info['categories']])
        rating = str(info['rating'])
        location = ','.join(info['location']['display_address'])
        latitude = info['coordinates']['latitude']
        longitude = info['coordinates']['longitude']
        photos = '|'.join(info['photos'])
        price = info['price'] if info.get('price') else ''
        try:
            start = info['hours'][0]['open'][0]['start']
        except:
            start = ''
        try:
            end = info['hours'][0]['open'][0]['end']
        except:
            end = ''
        transactions = '' if info['transactions'] == [] else '|'.join(info['transactions'])
        '''
        new_info = {}
        fields = ['ID', 'name', 'is_closed', 'url', 'phone', 'display_phone', 'review_count',\
                  'category', 'rating', 'location', 'latitude','longitude', 'photos', 'price',\
                  'start', 'end', 'transactions']
        for field in fields:
            new_info[field] = eval(field)
        '''
        new_info = (ID, name, is_closed, url, phone, display_phone, review_count,\
                    category, rating, location, latitude, longitude, photos,\
                    price, start, end, transactions)
        return new_info

def parse_business_reviews(info, business_id):
    ID = info['id']
    text = info['text']
    rating = str(info['rating'])
    time_created = info['time_created']
    userid = info['user']['id']
    username = info['user']['name']
    '''
    new_info = {}
    fields = ['ID', 'text', 'rating', 'time_created', 'userid', 'username']
    for field in fields:
        new_info[field] = eval(field)
    '''
    new_info = (business_id, ID, text, rating, time_created, userid, username)
    return new_info
