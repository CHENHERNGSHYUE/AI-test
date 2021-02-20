# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:06:28 2021

@author: chenmth
"""

'''
jieba是一個專業的分詞工具
'''

import jieba

def test_jieba(x):

    cut = jieba.cut(x)
    #print(cut)
    
    list_cut = list(cut)
    #print(list_cut)
    
    #arr = ''.join(list_cut)
    
    return list_cut
    
if __name__ == '__main__':
   print(test_jieba("我喜歡打籃球"))