# -*- coding: utf-8 -*-
# group 7

import numpy as np
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from g7_import_data import import_data


# Import recoded data
df = import_data(recoded=True)

# Delete duplicates and unrecoded labels
df.drop_duplicates(['title'], keep='last', inplace=True)
df = df[df['theme_recoded'] != 'delete']

# Join lemmatized words
df['list_lemma'] = df['list_lemma'].map(lambda x: ' '.join(x))

# Fix random seed for reproducibility
np.random.seed(10)

# Create the transform with tfidf strategy
vectorizer = TfidfVectorizer(max_df=0.80, min_df=2, max_features=10000)

# Tokenize and build vocabulary
vectorizer.fit(df['list_lemma'])
vocabulary = vectorizer.vocabulary_

# Encode document
xtrain = vectorizer.transform(df['list_lemma']).toarray()

dict_classes = {
            'international': 0,
            'france': 1,
            'economie': 2,
            'sciences_high_tech': 3,
            'arts_et_culture': 4,
            'sports': 5,
            'sante': 6
            }

# Recode our output
ytrain = df['theme_recoded'].map(dict_classes)

# Train our classifier
clf = SGDClassifier(loss='log', penalty='l2', alpha=1e-5, random_state=10,
                    max_iter=100, tol=None)
clf.fit(xtrain, ytrain)

# Save it in a pickle file
pickle.dump(vectorizer, open('g7_vectorizer', 'wb'))
pickle.dump(clf, open('g7_clf', 'wb'))
