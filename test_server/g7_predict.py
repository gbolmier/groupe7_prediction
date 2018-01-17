# -*- coding: utf-8 -*-
# group 7

import pandas as pd
import numpy as np
import requests
import pickle

from get_data.g7_import_data import import_data
from sklearn.decomposition import PCA


# Import our vectorizer and our classifier
vectorizer = pickle.load(open('supervised_learning/g7_vectorizer', 'rb'))
clf = pickle.load(open('supervised_learning/g7_clf', 'rb'))

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
post_db = [
        {"id_article": i, "label": j[0], "strongest_label": j[1]}
        for (i, j) in zip(df['id'], multi_labels)
        ]

#i = 0
#step = 1000
#url = 'http://130.120.8.250:5005/var/www/html/projet2018/code/bd_index/API_V2/index/label'
#
## Let's send multi-labels categories to the database with post requests
#while len(post_db) > i*step:
#    if len(post_db) - (i + 1)*step > 0:
#        r = requests.post(url=url, json=post_db[i*step:(i + 1)*step])
#        print(r.text)
#    else:
#        r = requests.post(url=url, json=post_db[i*step:len(post_db)])
#        print(r.text)
#    i = i + 1

# Prepare data for the non-supervised
multi_labels = [
        [dict_labels[i] for i, p in enumerate(probas) if p > 0.2]
        for probas in predicted_probas
        ]    
 
colnames = list(dict_labels.values())
data_non_supervised = pd.DataFrame(x_multi)

# Add themes with dummy variables
for name in colnames:
    data_non_supervised[name] = [int(name in elem) for elem in multi_labels]    

# Transform it into numpy array
data_non_supervised = data_non_supervised.values

# Let's do a pca to reduce our tfidf
tfidf = data_non_supervised[:, :10000]
rest = data_non_supervised[:, 10000:]
pca = PCA(n_components=10)
tfidf = pca.fit_transform(tfidf)

# Concatenate all
data_non_supervised = np.concatenate([tfidf, rest], axis=1)
pickle.dump(data_non_supervised, open('data_non_supervised', 'wb'))
