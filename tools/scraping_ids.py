#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:02:14 2021

@author: LiShuang
"""

import requests
import re
from urllib.parse import urlencode

HOST_URL = 'https://www.yelp.com/search?'

def get_response(find_desc, find_loc, start):
    params = {
                'find_desc': find_desc,
                'find_loc': find_loc,
                'start': str(start*10)
            }
    response = requests.get(HOST_URL, params)
    return response

def get_max_pages_num(find_desc, find_loc):
    r = get_response(find_desc, find_loc, start=0)
    pattern = '<div class=" border-color--default__09f24__1eOdn text-align--center__09f24__1P1jK"><span class=" css-e81eai">(.*?)</span></div>'
    max_page = re.findall(pattern, r.text)[0].split(' ')[-1]
    max_page = int(max_page)
    return max_page

def get_all_business_ids(find_desc, find_loc, amounts):
    max_pages = get_max_pages_num(find_desc, find_loc)
    if int(amounts / 10) > max_pages:
        print('The required number exceeds the maximum numbers available! ')
    else:
        max_pages = int(amounts / 10)
    business_ids = []
    for page in range(max_pages):
        r = get_response(find_desc, find_loc, start=page)
        pattern = r'"bizId":"(.*?)",'
        tmp_ids = re.findall(pattern, r.text)
        business_ids.extend(tmp_ids)
    return business_ids
