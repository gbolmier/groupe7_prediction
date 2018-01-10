#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 10:29:24 2018

@author: AntoineP
"""

import json as js
import os


path = "C:/Users/pouch/Desktop/Projet IP2018/lefigaro" #Chemin vers le dossier contenant les articles
for file in os.listdir(path):
    article = js.load(open(path + "/" + file))
    print(article["theme"]) #Theme de l'article
    
#Creation du dictionnaire
                
categorie={'theme':'categorie', 'actualite france':'France','sciences': 'Science/High-tech','indices actions': 'delete','article':'delete','conjoncture':'Economie','conso':'Economie','emploi':'Economie','arts expositions':'Culture','fonds trackers':'Economie','programme tv':'Culture','culture':'Culture','musique':'Culture','langue francaise':'Culture','cinema':'Culture','livres':'Culture','automobile':'Science/High-tech','jardin':'delete','lifestyle':'delete','voyages':'delete','mode homme':'delete','gastronomie':'Gastronomie','le scan sport':'Sport','flash eco':'Economie','entrepreneur':'Economie','retraite':'delete','sortir paris':'Culture','jeux video':'Culture','horlogerie':'delete','emploi':'Economie','theatre':'Culture','assurance':'Economie','devises matieres premieres':'Economie','histoire':'Culture','bd':'Culture','vox':'delete','secteur':'Science/High-tech','politique':'Politique','social':'Politique',},
print(df['body'][df['theme'] == 'social'].values)
