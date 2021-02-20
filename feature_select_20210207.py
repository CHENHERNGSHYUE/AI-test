# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 15:28:42 2021

@author: chenmth
"""


'''
用來過濾變異數低的特徵

降維方式 (EX: 二元空間變一條線)
PCA (Principal Component Analysis) ，適合用在很大維度的情形下去降維
'''
from sklearn.feature_selection import VarianceThreshold

from sklearn.decomposition import PCA

arr = [[0,2,0,3], [0,1,4,3], [0,1,1,3]]

def fs():
    
    filt = VarianceThreshold(threshold=0.0)
    
    data = filt.fit_transform(arr)
    
    print(data)
    
def pca():
    
    pca_string = PCA(n_components=0.92)
    
    data = pca_string.fit_transform(arr)
    
    print(data)

if __name__ == '__main__':
    #fs()
    pca()