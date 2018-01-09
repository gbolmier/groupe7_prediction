# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 11:29:27 2018

@author: valen
"""

import json as js
import os
import pandas as pd
import glob


#path = "C:/Users/valen/OneDrive/Documents/projet_recodage_telerama/telerama" #Chemin vers le dossier contenant les articles
path= "C:/Users/valen/OneDrive/Documents/projet/target_press_article/telerama"
for file in os.listdir(path):
      article = js.load(open(path + "/" + file))
      print(article["theme"])
        
    

def import_data(folder):
    frames = []
    for file_path in glob.glob('%s/*.json' % path):
        article = pd.read_json(file_path, typ='series').to_frame('index').transpose()
        frames.append(article)
    df = pd.concat(frames)
    df.sort_values(by=['theme'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

#path = "C:/Users/valen/OneDrive/Documents/projet_recodage_telerama/telerama"
path="C:/Users/valen/OneDrive/Documents/projet/target_press_article/telerama"
df = import_data(path)
print(df)

# print themes labels
print(set(df['theme'].values))

# print article from a category
print(df['body'][df['theme'] == 'enfants'])
    
dict_telerama = {
        'livre':'Culture',
        'cinema':'Culture',
        'musique':'Culture',
        'series tv':'Culture',
        'radio':'Culture',
        'sortir':'France',
        'television':'Culture',
        'medias':'Culture',
        'monde':'International',
        'scenes':'Culture',
        'idees':'delete',
        'enfants':'delete'}

dict_telerama

#print article from a category
print(df['body'][df['theme'] == 'cinema'].values[0:2]) 

# Recode categories
df['new_cat'] = df['theme'].map(dict_telerama)

