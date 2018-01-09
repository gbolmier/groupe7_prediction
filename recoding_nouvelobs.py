# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 09:49:25 2018

@author: cmisid
"""

# les categories:
categories = [
        'international', # politique etrangere, voyage
        'politique fr', 
        'france', # actu fait divers en france NON POLITIQUE
        'economie', 
        'sciences/high-tech', # jeux video
        'arts et culture', # gastronomie, mode, arts, cinema, voyages, litterature
        'sports', # automobile
        'sante'
        ]

# importation des articles sous un dataframe    
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

path = "C:/Users/cmisid/Documents/ProjetInterPromo/article/nouvelobs"
df = import_data(path)
 
# print themes labels
print(set(df['theme'].values))  
# print article from a category
print(df['body'][df['theme'] == 'bd'].values)

#creation dico pour les articles correpondants au catégories
dico1 = {'monde':'international',
        'sante':'sante',
        'actualites':'delete',
        'cinema' : 'arts et culture', 
        'sciences' : 'sciences/high-tech',
        'voyage' : 'france',
        'mode' : 'arts et culture',
        'societe' : 'international',
        'lifestyle' : 'arts et culture',
        'notizie italiane' : 'delete',
        'edito':'arts etcculture',
        'sport': 'sports', 
        'faits divers': 'france',
        'high tech' : 'sciences/high-tech',
        'tech' : 'sciences/high-tech', 
        'food' : 'arts et culture',
        'pop life' : 'arts et culture',
        'l histoire du soir' : 'delete',
        'planete' : 'delete',
        'education' : 'arts et culture',
        'design':'international',
        'rue89':'france' ,
        'politique':'france' ,
        'bd':'arts et culture',
        'jeux video':'sciences/high-tech',
        'brexit':'international' ,
        'presidentielle 2017':'france' ,
        'documentaire':'delete',
        'documents':'delete',
        'idees':'arts et culture' ,
        'le grand oral':'delete', 'justice':'politique fr',
        'economie':'economie',
        'Culture':'arts et culture'}




# Nouvelles données  :importation des articles sous un dataframe 
def import_data(folder):
    frames = []
    for file_path in glob.glob('%s/*.json' % path):
        article = pd.read_json(file_path, typ='series').to_frame('index').transpose()
        frames.append(article)
    df = pd.concat(frames)
    df.sort_values(by=['theme'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

path = "C:/Users/cmisid/Documents/ProjetInterPromo/target_press_article/nouvelobs"
df = import_data(path)
 # print themes labels
print(set(df['theme'].values)) 
# print article from a category
print(df['content'][df['theme'] == 'l enquete de l obs'].values) 

dico2={'l humeur de jerome garcin':'international',
        'la selection teleobs' : 'delete',
        'sur le sentier des prix' : 'arts et culture', 
        'voyages lointains' : 'arts et culture', 
        'critique' : 'arts et culture',
        'theatre' : 'arts et culture',
        'people' : 'arts et culture',
        'attentats terroristes a paris' : 'france', 
        'emotion canada' : 'arts et culture',
        'series' : 'arts et culture',
        'auto moto' : 'sport',
        'info radio' : 'arts et culture',
        'beaux livres' : 'arts et culture', 
        'faits divers' : 'france',
        'read in the usa' : 'international',
        'en partenariat avec books' : 'arts et culture',
        'medias' : 'arts et culture', 
        'musique' : 'arts et culture',
        'l enquete de l obs' : 'delete', 
        'romans' : 'arts et culture',
        'art design' : 'arts et culture',
        'la selection teleobs' : 'delete',
        'sur le sentier des prix' : 'arts et culture', 
        'chroniques' : 'international', 
        'voyages lointains' : 'arts et culture', 
        'critique' : 'arts et culture',
        'theatre' : 'arts et culture',
        'people' : 'arts et culture'
}
dico = dict(dico1)
dico.update(dico2)
