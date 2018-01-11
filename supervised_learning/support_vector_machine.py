# -*- coding: utf-8 -*-
# group 7

import numpy as np
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.svm import SVC


# Import data
df = pickle.load(open('../../cleaned_df', 'rb'))

# Fix random seed for reproducibility
dic = {'politique fr':'france',
       'international':'international',
       'france': 'france',
       'economie': 'economie',
       'sciences/high-tech':'sciences/high-tech',
       'arts et culture':'arts et culture',
       'sports':'sports',
       'sante':'sante'
       }

df['theme'] = df['theme'].map(dic)

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


#Recode Class
dict_classes = {
           'international':0,
           'france':1,
           'economie':2,
           'sciences/high-tech':3,
           'arts et culture':4,
           'sports':5,
           'sante':6
       }

#Concatenate xtrain, ytrain and ytest and xtest
X= vectorizer.transform(df['content']).toarray()
Y= df['theme'].map(dict_classes)

# Recode our output
ytrain = ytrain.map(dict_classes)
ytest = ytest.map(dict_classes)

# Function modelization
def modelization(model, model_name):
    """
    Take a model and it's name in parameters, train a classifier and print the
    accuracy, the confusion matrix and print the precision (true positive/true positive + false positive), recall (true positive/true positive + false negative), f1-score for each target names .
    """
    clf = model.fit(xtrain, ytrain)
    predicted = clf.predict(xtest)
    print('\n--- %s results ---' % model_name)
    print('Accuracy score : %s' % accuracy_score(ytest, predicted))
    print('Confusion matrix :\n%s' % confusion_matrix(ytest, predicted))
    print('Labels score : \n%s' % classification_report(ytest, predicted))


modelization(OneVsRestClassifier(SVC(C=1.)), 'SVM one vs all')
modelization(OneVsOneClassifier(SVC(C=1.)), 'SVM one vs one')
modelization(OneVsOneClassifier(LinearSVC(C=1.)), 'Linear SVM one vs one')
modelization(OneVsRestClassifier(LinearSVC(C=1.)), 'Linear SVM one vs all')

# Find the best parameters for each model
def gridSearch(X,Y,parameters,model):
    clf = GridSearchCV(model, parameters)
    clf.fit(X, Y)
    print(clf.best_score_)
    print(clf.best_params_)

#gridSeach svm OnevsOne (The best parameters is C=1)
gridSearch(X,Y,{'estimator__C': [1, 10, 100, 1000]},OneVsOneClassifier(LinearSVC()))