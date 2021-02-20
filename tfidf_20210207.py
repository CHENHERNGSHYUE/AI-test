# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 10:52:43 2021

@author: chenmth
"""

'''
tf: 某詞語在文章中出現的頻率 (term frequency)
idf: 某詞語在文章中的重要性(importance of document frequency) = 總文章數/該詞出現在文章的總數
'''

from sklearn.feature_extraction.text import TfidfVectorizer # 判斷詞的重要性

import jieba_20210206 as sepWord

def tfidf(str1, str2, str3):
    tf = TfidfVectorizer()
    
    test1 = sepWord.test_jieba(str1)
    test2 = sepWord.test_jieba(str2)
    test3 = sepWord.test_jieba(str3)
    
    result1 = ' '.join(test1)
    result2 = ' '.join(test2)
    result3 = ' '.join(test3)
    
    data = tf.fit_transform([result1,result2,result3])
    
    print(tf.get_feature_names())
    
    print(data.toarray())
    

if __name__ == "__main__":
    tfidf("我喜歡打籃球","我喜歡跳舞","我很會下棋")