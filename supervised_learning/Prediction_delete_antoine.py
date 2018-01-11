#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:07:36 2018

@author: AntoineP
"""

import pickle
import pandas
 
test = pickle.load(open('../../cleaned_df', 'rb'))
model = pickle.load(open('../../modelgbm', 'rb'))

test = test[test['theme'] == 'delete']


predicted = model.predict(test)
predicted = predicted.argmax(1) #Proba to selected label

dict_inv_classes = {
            0: 'international',
            1:'france',
            2:'economie',
            3:'sciences/high-tech',
            4:'arts et culture',
            5:'sports',
            6:'sante'
        }
cat_pred = pd.Series(predicted).map(dict_inv_classes)

df = 
res = [
       
       
       
       ]


