#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
import pandas as pd
import glob


def import_data(folder):
    frames = []
    df = pd.DataFrame()
    # Load recoding dictionnaries
    all_dicts = pickle.load(open('./groupe7_prediction/PreProcessing/all_dicts', 'rb'))
    sites = ['lemonde', 'lefigaro', 'liberation', 'nouvelobs', 'telerama', 'futurasciences']
    for site,  site_dict in zip(sites, all_dicts):
        frames = []
        for file_path in glob.glob('%s/%s/*.json' % (path, site)):
            article = pd.read_json(file_path, typ='series').to_frame('index').transpose()
            frames.append(article)
    df = pd.concat(frames)
    df.sort_values(by=['theme'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

path = './data/target_press_article/'
df = import_data(path)

# Save our Dataframe with clean categories in a pickle file
pickle.dump(df, open('./data/recoded_df', 'wb'))

