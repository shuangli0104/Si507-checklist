#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 19:35:44 2021

@author: LiShuang
"""

import sqlite3
import sys
sys.path.append('tools/')
from tools.scraping_ids import get_all_business_ids
from tools.yelp_fusion import get_business
from tools.yelp_fusion import get_business_reviews
from tools.my_api_key  import API_KEY
from tools.sql_tools import *
from tools.parse_tools import *
import pandas as pd
import numpy as np

#%%
def main():
    while True:
        search_item = input('The restaurant you want to search(e.g. burgers, etc or exit: ')
        if search_item == 'exit':
            break
        search_place = input('The place you want to search(e.g. Hong Kong, etc or exit: ')
        if search_place == 'exit':
            break
        search_num = input('The number you want to search(P.S. Ten times, we suggest input less than 50): ')

        # get ids
        ids = get_all_business_ids(search_item, search_place, int(search_num))
        # print(ids)
        
        data = []
        for ID in ids:
            statement = select_statement('Details', ID)
            select_result = execute_sql(statement)
            if select_result == []:
                print('Fetching...')
                tmp_data = get_business(API_KEY, ID)
                tmp_data = parse_business_details(tmp_data)
            
                if tmp_data == '':
                    ids.remove(ID)
                    continue
                else:
                    statement = insert_statement('Details', tmp_data)
                    execute_sql(statement)
                    data.append(tmp_data)
            else:
                print('Using Cache...')
                data.append(select_result[0])
        
        data = pd.DataFrame(data, columns=['Business_id', 'Name', 'is_closed',\
                                           'url', 'phone', 'display_phoone',\
                                           'review_count', 'category', 'rating',\
                                           'location', 'latitude', 'longitude',\
                                           'photos', 'price', 'start', 'end',\
                                           'transactions'], index=np.arange(1, len(data)+1))
        print('We found the following results...')
        print(data['Name'])
        review_NO = input('Pleased input the number and we will show the reviews(or exit): ')
        if review_NO == 'exit':
            break
        else:
            review_NO = int(review_NO)
            ID = data.loc[review_NO, 'Business_id']
            statement = select_statement('Reviews', ID)
            select_result = execute_sql(statement)
            review_data = []
            if select_result == []:
                print('Fetching...')
                tmp_data = get_business_reviews(API_KEY, ID)
                for review in tmp_data['reviews']:
                    TMP = parse_business_reviews(review, ID)
                    statement = insert_statement('Reviews', TMP)
                    execute_sql(statement)
                    review_data.append(TMP)
                
            else:
                print('Using Cache...')
                review_data.append(select_result[0])

        review_data = pd.DataFrame(review_data, columns=['Business_id', 'Review_id', 'Text',\
                                                         'Rating', 'Time_created', 'UserId',\
                                                         'Username'], index=np.arange(1, len(review_data)+1))
        print(review_data)
        
        
        
        
            

if __name__ == "__main__":
    main()
statement2 = '''
                CREATE TABLE Reviews
                (
                Business_id varchar(255) NOT NULL,
                Review_id varchar(255) NOT NULL,
                Text varchar(255),
                Rating varchar(255),
                Time_created varchar(255),
                Userid varchar(255),
                Username varchar(255),
                FOREIGN KEY (Business_id) REFERENCES Details(Business_id)
                )
                '''







