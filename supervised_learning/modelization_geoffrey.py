# -*- coding: utf-8 -*-
# group 7

import numpy as np
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.svm import SVC


# Import data
df = pickle.load(open('../../cleaned_df', 'rb'))

# Fix random seed for reproducibility
np.random.seed(10)

# Split our df for train/test with a stratify strategy
xtrain, xtest, ytrain, ytest = train_test_split(df, df['theme'], test_size=0.2,
                                                stratify=df['theme'])

# Create the transform with tfidf strategy
vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=10000)
# Tokenize and build vocabulary
vectorizer.fit(xtrain['content'])
vocabulary = vectorizer.vocabulary_
# Encode document
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

# Recode our output
ytrain = ytrain.map(dict_classes)
ytest = ytest.map(dict_classes)

def modelization(model, model_name):
    """
    Take a model and it's name in parameters, train a classifier and print the
    accuracy score and the confusion matrix.
    """
    clf = model.fit(xtrain, ytrain)
    predicted = clf.predict(xtest)
    print('\n--- %s results ---' % model_name)
    print('Accuracy score : %s' % accuracy_score(ytest, predicted))
    print('Confusion matrix :\n%s' % confusion_matrix(ytest, predicted))


modelization(MultinomialNB(), 'Naive Bayes')
#modelization(OneVsRestClassifier(SVC(C=1.)), 'SVM one vs all')
#modelization(OneVsOneClassifier(LinearSVC(C=1.)), 'Linear SVM one vs one')