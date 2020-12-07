# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:36:36 2020

@author: wayne
"""

drive = str(input('你有開過車嗎? '))
if drive !="有" and drive !="沒有":
    print('只能輸入有或沒有')
    raise SystemExit
        
age = int(input('年齡呢?'))
if drive == "是":
    if age >=18:
        print ('可以開車')
    else:
        print('不可以這樣喔')
elif age <18:
    print('不可以學開車')
else:
    print('可以學開車')

