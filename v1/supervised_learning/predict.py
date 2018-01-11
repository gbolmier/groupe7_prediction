# -*- coding: utf-8 -*-
# group 7

import requests
import pickle


# Import our classifier and articles to predict
clf = pickle.load(open('clf', 'rb'))