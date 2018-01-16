# -*- coding: utf-8 -*-
# group 7

import numpy as np
import pickle
import lightgbm as lgb
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.svm import LinearSVC
from sklearn.svm import SVC


# Import data
df = pickle.load(open('../../cleaned_df', 'rb'))

#Supprimer les articles avec la catégorie manquante
df = df[df['theme']!= 'delete']

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


dict_classes = {
            'international':0,
            'france':1,
            'economie':2,
            'sciences/high-tech':3,
            'arts et culture':4,
            'sports':5,
            'sante':6
        }
ytrain = ytrain.map(dict_classes)
ytest = ytest.map(dict_classes)

lgb_train = lgb.Dataset(xtrain, ytrain)
lgb_eval = lgb.Dataset(xtest, ytest, reference=lgb_train)



# Recode our output


best= {'bagging_fraction': 0.95,
 'feature_fraction': 1.0,
 'num_leaves': 20,
 'reg_alpha': 0.5,
 'metric': 'multi_error',
 'application': 'multiclass',
 'learning_rate': [0.1], 
 'bagging_seed': 1,
 'feature_fraction_seed': 2, 
 'num_class': 7}



gbm = lgb.train(best,
                lgb_train,
                num_boost_round=750,
                valid_sets=lgb_eval,
                early_stopping_rounds=100)


predicted = gbm.predict(xtest)
predicted = predicted.argmax(1) #Proba to selected label

print('Accuracy score : %s' % accuracy_score(ytest, predicted))
print('Confusion matrix :\n%s' % confusion_matrix(ytest, predicted))
print(metrics.classification_report(ytest, predicted, target_names=labels))

