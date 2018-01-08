#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 10:29:24 2018

@author: AntoineP
"""

import json as js
import os


path = "./lemonde" #Chemin vers le dossier contenant les articles
for file in os.listdir(path):
    article = js.load(open(path + "/" + file))
    print(article["theme"]) #Theme de l'article
    
                
                    
                    