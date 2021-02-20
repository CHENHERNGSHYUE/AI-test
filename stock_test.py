# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:34:49 2020

@author: chenmth
"""

import twstock
import matplotlib.pyplot as plt
import numpy as np

stock = twstock.Stock('2330')

h = stock.high[-1:] #高點
print(h)

l = stock.low #低點
print(l)

e = stock.price #收盤價
print(e) 

s = stock.open #開盤價
print(s)
