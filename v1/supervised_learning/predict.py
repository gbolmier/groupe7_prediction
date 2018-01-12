# -*- coding: utf-8 -*-
# group 7

import pickle
import pandas as pd
import json


# Import our classifier and articles to predict
model = pickle.load(open('clf', 'rb'))

test = pickle.load(open('../pre_processing/recoded_df', 'rb'))
vectorizer = pickle.load(open('vectorizer', 'rb'))

#test = test[test['theme'] == 'delete']

test_vec = vectorizer.transform(test['list_lemma']).toarray()


predicted = model.predict(test_vec)
#predicted = predicted.argmax(1) #Proba to selected label

dict_inv_classes = {
            0:'international',
            1:'france',
            2:'economie',
            3:'sciences_high_tech',
            4:'arts_et_culture',
            5:'sports',
            6:'sante'
        }
cat_pred = pd.Series(predicted).map(dict_inv_classes)


res = [
       
       { str(i): j} for (i,j) in zip(test['id'],cat_pred)  
       
       ]



#import json
#
#for js in res:
#    print(js)
#    with open('a' + '.json', 'w') as fp:
#        json.dump(js, fp)   
#        
#        

res = [{1:'sante'}, {2:'sciences_high_tech'}]
import requests
r = requests.post('http:///post', data = res)