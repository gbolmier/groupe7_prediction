# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 09:06:06 2018

@author: pouch
"""
#Groupe7

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

path = "C:/Users/pouch/Desktop/Projet IP2018/lefigaro"
df = import_data(path)

# print themes labels
print(set(df['theme'].values))

print(df['content'][df['theme'] == 'vie bureau'].values[0:2])

dict_figaro = {
        'vox':'delete',
        'bd':'arts et culture',
        'culture':'arts et culture',
        'secteur':'sciences/high-tech',
        'actualite france':'france',
        'derives':'sciences/high-tech',
        'emploi':'economie',
        'langue francaise':'arts et culture',
        'expertise':'economie',
        'sortir paris':'arts et culture',
        'equitation':'sport',
        'devises matieres premieres':'economie',
        'social':'arts et culture',
        'sciences':'sciences/high-tech',
        'cinema':'arts et culture',
        'vie bureau':'delete',
        'societes':'economie',
        'jardin':'arts et culture',
        'musique':'arts et culture',
        'automobile':'sciences/high-tech',
        'politique':'politique fr',
        'voyages':'arts et culture',
        'flash eco':'economie',
        'horlogerie':'delete',
        'histoire':'arts et culture',
        'arts expositions':'arts et culture',
        'gastronomie':'arts et culture',
        'retraite':'economie',
        'conso':'economie',
        'indices actions':'economie',
        'theatre':'arts et culture',
        'jeux video':'sciences/high-tech',
        'mode homme':'arts et culture',
        'lifestyle':'arts et culture',
        'le scan sport':'sports',
        'livres':'arts et culture',
        'programme tv':'arts et culture',
        'fonds trackers':'economie',
        'entrepreneur':'delete',
        'assurance':'delete',
        'elections':'politique fr',
        'medias':'arts et culture',
        'conjoncture':'economie',
        'article':'delete',
    
        }
