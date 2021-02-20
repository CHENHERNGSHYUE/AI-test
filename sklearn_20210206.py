# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 23:30:38 2021

@author: chenmth
"""

'''
sklearn是做"特徵擷取的動作"
可對dict擷取也可對text擷取 (但不支持中文)，主要以空格判斷
特徵擷取主要用來對非數字或單英(中)文字母外的內容轉換成向量數字
'''

from sklearn.feature_extraction import DictVectorizer # dict特徵
from sklearn.feature_extraction.text import CountVectorizer # 文本特徵

import jieba_20210206

def vect(x):
    cv = CountVectorizer()
    
    test = jieba_20210206.test_jieba(x)
    
    data = cv.fit_transform(test)
    
    print(cv.get_feature_names())
    

if __name__ == "__main__":
    vect("我喜歡打籃球")