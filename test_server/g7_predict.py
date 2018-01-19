# -*- coding: utf-8 -*-
# group 7

import pandas as pd
import numpy as np
import pickle
import json

from g7_import_data import import_data
from sklearn.decomposition import PCA


# Import our vectorizer and our classifier
vectorizer = pickle.load(open('g7_vectorizer', 'rb'))
clf = pickle.load(open('g7_clf', 'rb'))

# Import recoded data
df = import_data(recoded=True, to_predict=True)

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

# Save it in a json file for the database
with open('g7_themes_multi_labels.json', 'w') as f:
    json.dump(post_db, f)

# Prepare data for the non-supervised
multi_labels = [
        [dict_labels[i] for i, p in enumerate(probas) if p > 0.2]
        for probas in predicted_probas
        ]

cols_semantic = ['rate_angry', 'rate_surprise', 'rate_positivity', 'rate_joy',
                 'rate_negativity', 'rate_fear', 'rate_sadness', 'rate_disgust',
                 'rate_subjectivity']


themes = list(dict_labels.values())
data_non_supervised = pd.DataFrame(x_multi)
data_non_supervised = pd.concat([data_non_supervised, df[cols_semantic]], axis=1)

# Add themes with dummy variables
for theme in themes:
    data_non_supervised[theme] = [int(theme in elem) for elem in multi_labels]

# Transform it into numpy array
data_non_supervised = data_non_supervised.values
data_non_supervised = np.array(data_non_supervised, float)

# Let's do a pca to reduce our tfidf
tfidf = data_non_supervised[:, :10000]
rest = data_non_supervised[:, 10000:]
pca = PCA(n_components=10, random_state=10)
tfidf = pca.fit_transform(tfidf)

# Concatenate all
data_non_supervised = np.concatenate([tfidf, rest], axis=1)
pickle.dump(data_non_supervised, open('data_non_supervised', 'wb'))

#kmeans = pickle.load(open('g7_k_means', 'rb'))
#dict_clusters = {0: 'cluster0', 1: 'cluster1', 2: 'cluster2', 3: 'cluster3',
#                 4: 'cluster4', 5: 'cluster5'}
#labels = kmeans.predict(data)
#labels = pd.Series(labels)
#labels = labels.map(dict_clusters)
