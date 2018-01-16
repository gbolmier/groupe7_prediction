# -*- coding: utf-8 -*-
# group 7

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
        0: 'international',
        1: 'france',
        2: 'economie',
        3: 'sciences_high_tech',
        4: 'arts_et_culture',
        5: 'sports',
        6: 'sante'
        }

# Get multi-labels list and list boolean for strongest label
multi_labels = [
           [[dict_labels[i] for i, p in enumerate(probas) if p > 0.2],
             [int(i == probas.argmax()) for i, p in enumerate(probas) if p > 0.2]]
           for probas in predicted_probas
       ]

# Create our list of dictionaries with the good format for the database
res = [
       {"id_article": i, "label": j[0], "strongest_label": j[1]}
       for (i, j) in zip(df['id'], multi_labels)
       ]

i = 0
step = 1000
url = 'http://130.120.8.250:5005/var/www/html/projet2018/code/bd_index/API_V2/index/label'

# Let's send our results to the database with a post request by 1000 articles
while len(res) > i*step:
    if len(res) - (i + 1)*step > 0:
        r = requests.post(url=url, json=res[i*step:(i + 1)*step])
        print(r.text)
    else:
        r = requests.post(url=url, json=res[i*step:len(res)])
        print(r.text)
    i = i + 1
