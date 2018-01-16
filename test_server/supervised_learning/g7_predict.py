# -*- coding: utf-8 -*-
# group 7

import pandas as pd
import requests
import pickle
import sys
sys.path.insert(0, "..")

from get_data.g7_import_data import import_data


# Import our vectorizer and our classifier
vectorizer = pickle.load(open('g7_vectorizer', 'rb'))
clf = pickle.load(open('g7_clf', 'rb'))

# Import recoded data
df = import_data(recoded=True)

# Join lemmatized words
df['list_lemma'] = df['list_lemma'].map(lambda x: ' '.join(x))

# Prepare our inputs
x_multi = vectorizer.transform(df['list_lemma']).toarray()

# Predict new labels
predicted_probas = clf.predict_proba(x_multi)

dict_labels = {
        0:'international',
        1:'france',
        2:'economie',
        3:'sciences_high_tech',
        4:'arts_et_culture',
        5:'sports',
        6:'sante'
        }

# Get multi-labels list and list boolean for strongest label
multi_labels = [
           [[dict_labels[i] for i, p in enumerate(probas) if p > 0.2],
             [int(i == probas.argmax()) for i, p in enumerate(probas) if p > 0.2]]
       for probas in predicted_probas
       ]

# Put it in json format
res = [
       { "id_article":i, "label": j[0], "strongest_label":j[1]} for (i,j) in zip(df['id'], multi_labels)
       ]
           
url ='http://130.120.8.250:5005/var/www/html/projet2018/code/bd_index/API/index/belong'
r = requests.post(url=url, json=res[0:2])
print(r.text)
r = requests.post(url=url, json=[res[2]])
print(r.text)