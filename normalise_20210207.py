# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:39:50 2021

@author: chenmth
"""

'''
第一種 歸一化 standarization
x' = (x-min)/(max-min) and x" = x'(mx - mi)+mi (default mx=1, mi=0)
缺點: 會受異常點影響最大最小值

第二種 標準化
x' = (x-平均值)/標準差

缺失值填補: 統一使用np.nan，如果是?、null、None，一律replace成np.nan
通常缺失值(np.nan)是填補平均數

scaler: 數量
'''

from sklearn.preprocessing import MinMaxScaler #歸一化
from sklearn.preprocessing import StandardScaler #標準化

from sklearn.impute import SimpleImputer as Imputer #缺失值填補
import numpy as np

def im():
    
    im = Imputer(missing_values=np.nan, strategy='mean')
    
    data = im.fit_transform([[1,2], [np.nan,3], [7,np.nan]]) #np.nan is float type
    
    print(data)
    
if __name__ == '__main__':
    im()