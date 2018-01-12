# -*- coding: utf-8 -*-
# group 7

import pandas as pd
import pickle
import glob


"""
A modifier pour le serveur :
    _ Mettre le vrai id
    _ Orthographes des sources dans les json
    _ Path complet pour aller dans le répertoire des json du groupe 6
"""

def import_data(path):
    """
    Take in parameter the path where the articles are and return a Dataframe of
    them with their id, source, title, theme, and list_lemma.
    """
    frames = []
    for file_path in glob.glob('%s/*.json' % path):
        article = pd.read_json(file_path, typ='series')
        article = pd.Series({'id':article['title'], 'source':article['newspaper'],
                             'theme':article['theme'], 'title':article['title'],
                             'list_lemma':article['content']['list_lemma']
                             })
        article = article.to_frame('index').transpose()
        frames.append(article)
        df = pd.concat(frames)
    df.drop_duplicates(['title'], keep='last', inplace=True)
    df.sort_values(by=['source'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


def recode_data(df):
    """
    Take in parameter the Dataframe of the articles and return it with recoded
    categories.
    """
    df_recoded = pd.DataFrame()
    # Load recoding dictionnaries
    all_dicts = pickle.load(open('all_dicts', 'rb'))
    sources = ['lemonde', 'lefigaro', 'liberation', 'nouvelobs', 'telerama',
               'Futura Sciences']
    # Let's recode each source one by one
    for source, source_dict in zip(sources, all_dicts):
        source_df = df[df['source'] == source]
        # Recode categories from the source
        source_df['theme'] = source_df['theme'].map(source_dict)
        # Concatenate with other sources in a single Dataframe
        df_recoded = pd.concat([df_recoded, source_df])
    df_recoded = df_recoded[df_recoded['theme'] != 'delete']
    df_recoded['list_lemma'] = df_recoded['list_lemma'].map(lambda x: ' '.join(x))
    df.reset_index(drop=True, inplace=True)
    return df_recoded


path = '../json_examples'
df = import_data(path)
df = recode_data(df)

# Save our Dataframe with clean categories in a pickle file
pickle.dump(df, open('recoded_df', 'wb'))