# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 20:38:44 2021

@author: chenmth
"""

'''
knn適用樣本數為己千到幾萬
但內存開銷大
'''

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from sklearn.preprocessing import StandardScaler


#df_feature = pd.read_excel('data.xlsx', usecols=["num1","num2","num3","num4","num5","num6"])
df_feature = pd.read_excel('data.xlsx', usecols=["month","day"])#輸入欄位
data = df_feature.values.tolist()

df_target = pd.read_excel('data.xlsx', usecols=["special"])#輸出欄位
target_pre = df_target.values.tolist()
target = []
for i in range(len(target_pre)):
    target.append(target_pre[i][0])

x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2)

#標準化看看(沒啥用的)
# std = StandardScaler()
# x_train = std.fit_transform(x_train)
# x_test = std.transform(x_test)

def knn():
    
    knn = KNeighborsClassifier(n_neighbors=50)
    knn.fit(x_train, y_train)
    
    y_predict = knn.predict(x_test)
    print("預測結果: " , y_predict)
    
    print("預測準確率為: ", knn.score(x_test, y_test))
   
if __name__ == '__main__':
    knn()    