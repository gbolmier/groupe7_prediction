# -*- coding: utf-8 -*-
# group 7

import numpy as np
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


"""
A modifier pour le serveur :
    _ Mettre le vrai classifieur
"""

# Import data
df = pickle.load(open('../pre_processing/recoded_df', 'rb'))  

# Fix random seed for reproducibility
np.random.seed(10)

# Create the transform with tfidf strategy
vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=10000, stop_words=['.'])
# Tokenize and build vocabulary
vectorizer.fit(df['list_lemma'])
vocabulary = vectorizer.vocabulary_
# Encode document
xtrain = vectorizer.transform(df['list_lemma']).toarray()

dict_classes = {
            'international':0,
            'france':1,
            'economie':2,
            'sciences/high-tech':3,
            'arts et culture':4,
            'sports':5,
            'sante':6
            }

# Recode our output
ytrain = df['theme'].map(dict_classes)

# Train our classifier
clf = MultinomialNB().fit(xtrain, ytrain)

# Save it in a pickle file
pickle.dump(clf, open('clf', 'wb'))