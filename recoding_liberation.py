##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Mon Jan  8 10:29:24 2018
#
#@author: AntoineP
#"""
#
#import json as js
#import os
#
#
#path = "C:/Users/Cassandre/Documents/articles/liberation" #Chemin vers le dossier contenant les articles
#for file in os.listdir(path):
#    article = js.load(open(path + "/" + file))    
#    print(article["theme"]) #Theme de l'article
#    
#    
#categories=dict()
#categories={'planete':'Science/High-tech','france':'France', 'sports':'Sport',
#            'desintox':'Santé', 'debats':'delete', 'elections presidentielle legislatives 2017':'France',
#            'futurs':'Science/High-tech','une saison a la montagne':'delete',
#            'chroniques':'delete','redecouvrir athenes':'International'}



import pandas as pd 
import glob 
 
 
def import_data(folder): 
    frames = [] 
    for file_path in glob.glob('%s/*.json' % path): 
        article = pd.read_json(file_path, typ='series').to_frame('index').transpose() 
        frames.append(article) 
    df = pd.concat(frames) 
    df.sort_values(by=['theme'], inplace=True) 
    df.reset_index(drop=True, inplace=True) 
    return df 
 
path = "C:/Users/Cassandre/Documents/robot_8.1/target_press_article/liberation" #Chemin vers le dossier contenant les articles
df = import_data(path) 
 
# print themes labels 
print(set(df['theme'].values)) 

categories=dict()
categories={'planete':'sciences/high-tech',
            'france':'france', 
            'sports':'sports',
            'desintox':'delete', 
            'debats':'delete', 
            'elections presidentielle legislatives 2017':'politique fr',
            'futurs':'delete',
            'une saison a la montagne':'delete',
            'chroniques':'delete',
            'redecouvrir athenes':'arts et culture',
            'photographie':'arts et culture',
            'sciences':'sciences/high-tech',
            'evenements libe':'delete',
            'voyage au coeur de lIA':'sciences/high-tech',
            'politiques':'politique fr',
            'sous le soleil exactement':'delete',
            'voyages':'arts et culture',
            'checknew':'delete',
            'saison en hiver':'delete'
            }


df['new_cat'] = df['theme'].map(categories)
