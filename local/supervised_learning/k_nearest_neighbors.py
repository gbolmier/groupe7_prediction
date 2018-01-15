# -*- coding: utf-8 -*-
# group 7

import pickle

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


###########                 FINAL MODEL ASSESSMENT                  ###########

# Import data for final model assessment (with train/test where test sample was
# not used during grid search)
xtrain, xtest, ytrain, ytest = pickle.load(open('../../../train_test_data_group7', 'rb'))

def model_assessment(model, model_name):
    """
    Take a model and it's name in parameters, train a classifier and print the
    classification report and the confusion matrix.
    """
    labels = ['international', 'france', 'economie', 'sciences_high_tech',
              'arts_et_culture', 'sports', 'sante']
    clf = model.fit(xtrain, ytrain)
    predicted = clf.predict(xtest)
    print('--- %s results ---\n' % model_name)
    print(metrics.classification_report(ytest, predicted, target_names=labels))
    print('Confusion matrix:\n%s' % metrics.confusion_matrix(ytest, predicted))


model_assessment(KNeighborsClassifier(n_neighbors=15), 'K Nearest Neighbors')