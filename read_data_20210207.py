# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:03:19 2021

@author: chenmth
"""

import pandas as pd

from sklearn.model_selection import train_test_split

# df = pd.read_excel('data.xlsx')
# #print(df) # show excel format

# print(df.day)

# #to list
# data = df.values.tolist()
# #print(data)

df_feature = pd.read_excel('data.xlsx', usecols=["num1","num2","num3","num4","num5","num6"])
data = df_feature.values.tolist()
#print(data)

df_target = pd.read_excel('data.xlsx', usecols=["special"])
target_pre = df_target.values.tolist()
target = []
for i in range(len(target_pre)):
    target.append(target_pre[i][0])
#print(target)

x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.25)

print(x_train,y_train)
print("========================================================================")
print(x_test,y_test)