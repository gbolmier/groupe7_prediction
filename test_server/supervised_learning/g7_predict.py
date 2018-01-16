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

# Separate articles we want to predict the themes than articles already recoded
already_recoded = df.loc[df['theme_recoded'] != 'delete'].copy()
to_recode = df.loc[df['theme_recoded'] == 'delete'].copy()

# Prepare our inputs
xtrain = vectorizer.transform(to_recode['list_lemma']).toarray()

# Predict new labels
predicted = clf.predict(xtrain)
predicted_probas = clf.predict_proba(xtrain)

dict_labels = {
        0:'international',
        1:'france',
        2:'economie',
        3:'sciences_high_tech',
        4:'arts_et_culture',
        5:'sports',
        6:'sante'
        }

# Recode to mono-label
to_recode.reset_index(drop=True, inplace=True)
to_recode.loc[:, 'theme_recoded'] = pd.Series(predicted).map(dict_labels)
df_recoded = pd.concat([already_recoded, to_recode])

# Get multi-labels id
multi_labels = [
        [
                i
                if p > 0.2
                ]
        [
                i
                if p == probas.argmax()
                ]
        for i, p in enumerate(probas) for probas in predicted_probas
        ]

## Recode multi-labels id to string
#multi_labels = [
#        [
#                dict_labels[label] for label in labels
#                ]
#        for labels in multi_labels
#        ]
#
#
#
#res = [
#       {"id_article": i, "label": j, "strongest_label": k}
#       for (i, j, k) in zip(df_recoded.id, df_recoded.theme_recoded,
#           df_recoded.strongest_label)
#       ]