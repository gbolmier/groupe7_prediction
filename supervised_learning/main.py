#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:48:47 2018

@author: AntoineP
"""
import time
main()
ac_time = time.localtime() #Récupérer date actuelle
daily_dir = ac_time. #Former le nom du dossier contenant les articles du jour avex la date du jour

#Recoder les catégories avec celle du dico et mettre 'delete' pour celles à predire. Prend en entrée le répertoire à traiter
#Objet init avec le dossier du jour,
recoding() 


text_filtering() #Nettoyer le texte

#Au lieu de faire 2 CRON, l'un pour prédire (quotidien) l'autre pour re-générer le corpus d'apprentissage (hebdomadaire),
#on peut mettre la maj hebdo dans un if (par exemple, if day = dimanche alors maj hebdo) 

if ac_time.tm_wday == 7: #7eme jour de la semaine
    modelisation()

predict()
send_to_bd()