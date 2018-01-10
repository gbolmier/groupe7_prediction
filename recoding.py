# -*- coding: utf-8 -*-
# groupe 7

import pandas as pd
import pickle
import glob


def recode_data(path):
    """
    Take in parameter the path where the articles are and return a Dataframe of
    them with recoded categories.
    """
    frames = []
    df = pd.DataFrame()
    # Load recoding dictionnaries
    all_dicts = pickle.load(open('all_dicts', 'rb'))
    sites = ['lemonde', 'lefigaro', 'liberation', 'nouvelobs', 'telerama', 'futurasciences']
    for site,  site_dict in zip(sites, all_dicts):
        frames = []
        for file_path in glob.glob('%s/%s/*.json' % (path, site)):
            # Read the article, transform it in Dataframe, then transpose it
            article = pd.read_json(file_path, typ='series').to_frame('index').transpose()
            frames.append(article)
        # Concatenante all articles from the site in a single Dataframe
        frames = pd.concat(frames)
        # Recode categories from the site
        frames['theme'] = frames['theme'].map(site_dict)
        # Concatenate with other sites in a single Dataframe
        df = pd.concat([df, frames])
    df.drop_duplicates(['title'], keep='last', inplace=True)
    df = df[df['theme'] != 'delete']
    df.sort_values(by=['theme'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


path = '/home/sidu1/Documents/Projet inter-promo 2018/target_press_article/'
df = recode_data(path)

# Save our Dataframe with clean categories in a pickle file
pickle.dump(df, open('../recoded_df', 'wb'))
