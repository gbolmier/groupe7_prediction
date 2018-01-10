# -*- coding: utf-8 -*-
# groupe 7

import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


# Import data
df = pickle.load(open('../cleaned_df', 'rb'))

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

def classes_to_vector(Y_output):
    output = []
    classes = [
            'international',
            'politique fr',
            'france',
            'economie',
            'sciences/high-tech',
            'arts et culture',
            'sports',
            'sante'
            ]
    # create an empty array for our output
    output_empty = [0] * len(classes)
    for i in Y_output:
        # output is a '0' for each tag and '1' for current tag
        output_row = list(output_empty)
        output_row[classes.index(i)] = 1
        output.append(output_row)
    Y_output = output
    return Y_output

# transform our classes in vectors of numbers
ytrain = classes_to_vector(ytrain)
ytest = classes_to_vector(ytest)
