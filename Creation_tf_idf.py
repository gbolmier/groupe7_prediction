#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 16:29:45 2018

@author: AntoineP
"""

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

df  = pickle.load(open('Tokenized_body.p', 'rb'))


for i in range(len(df)):
    df['body'][i] = ' '.join(df['body'][i])



tfidf_gl = TfidfVectorizer(max_df=0.95, min_df=2, max_features=10000) 

tfidf_gl_t = tfidf_gl.fit_transform(df['body'])



