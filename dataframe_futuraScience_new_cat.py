# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 13:54:20 2018

@author: valen
"""

import json as js
import os
import pandas as pd
import glob

#path = "C:/Users/valen/OneDrive/Documents/projet_recodage_telerama/futurasciences" #Chemin vers le dossier contenant les articles
path="C:/Users/valen/OneDrive/Documents/target_press_article/futurasciences"
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

#path = "C:/Users/valen/OneDrive/Documents/projet_recodage_telerama/futurasciences"
path="C:/Users/valen/OneDrive/Documents/target_press_article/futurasciences"
df_futurascience = import_data(path)
print(df_futurascience)

# print themes labels
print(set(df_futurascience['theme'].values))

# print article from a category
print(df_futurascience['body'][df_futurascience['theme'] == 'enfants'])

dico_futurascience= {
        'tech':'Science/High-tech',
        'sciences':'Science/High-tech',
        'planete':'Science/High-tech',
        'sante':'Santé',
        'maison':'Science/High-tech'
        }

#print article from a category
print(df_futurascience['body'][df_futurascience['theme'] == 'sante'].values[0:2]) 

# Recode categories
df_futurascience['new_cat'] = df_futurascience['theme'].map(dico_futurascience)