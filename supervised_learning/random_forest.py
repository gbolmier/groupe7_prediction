# -*- coding: utf-8 -*-
# group 7

import numpy as np
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz


# Import data
df = pickle.load(open('./cleaned_df', 'rb'))


recode_dict = {
        'international':'international',
        'politique fr':'france',
        'france':'france',
        'economie':'economie',
        'sciences/high-tech':'sciences/high-tech',
        'arts et culture':'arts et culture',
        'sports':'sports',
        'sante':'sante'
        }

df['theme'] = df['theme'].map(recode_dict)

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
    print('Precision matrix :\n%s' % classification_report(ytest,predicted))


#DecisionTreeRegressor
clf = DecisionTreeRegressor(min_samples_leaf=10, max_depth=3)
clf = clf.fit(xtrain,ytrain)
clf.score(xtrain,ytrain)
#export_graphviz(clf, out_file="arbre.dot")

# Let's find best parameters for our model
parameters = {'n_estimators':[50, 100, 500], 'max_depth':[4, 6, 8]}
clf = GridSearchCV(RandomForestClassifier(), parameters, cv=5, verbose=1)
clf.fit(xtrain, ytrain)
print(clf.best_score_)
print(clf.best_params_)

# best random forest
modelization(RandomForestClassifier(n_estimators=500, max_depth=8),'Random Forest')