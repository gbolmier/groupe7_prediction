# -*- coding: utf-8 -*-
# groupe 7

import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# Import data
df = pickle.load(open('./data/cleaned_df', 'rb'))

# split
xtrain, xtest, ytrain, ytest = train_test_split(df, df['theme'], train_size=0.8,
                                                stratify=df['theme'])

# create the transform
vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=10000)
# tokenize and build vocab
vectorizer.fit(xtrain['content'])
# summarize
vocabulary = vectorizer.vocabulary_
# encode document
xtrain = vectorizer.transform(xtrain['content']).toarray()
xtest = vectorizer.transform(xtest['content']).toarray()

dict_classes = {
            'international':0,
            'politique fr':1,
            'france':2,
            'economie':3,
            'sciences/high-tech':4,
            'arts et culture':5,
            'sports':6,
            'sante':7
        }

ytrain = ytrain.map(dict_classes)
ytest = ytest.map(dict_classes)

# Modelize a Naive Bayes
clf = MultinomialNB().fit(xtrain, ytrain)
# predict
predicted = clf.predict(xtest)
# print our score
print(accuracy_score(ytest, predicted))