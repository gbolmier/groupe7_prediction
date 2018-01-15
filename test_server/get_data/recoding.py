# -*- coding: utf-8 -*-
# group 7

import pandas as pd
import pickle
import glob


def import_data(path):
    """
    Take in parameter the path where the articles are located and return a 
    Dataframe of them with these columns: id, source, title, theme, and list_lemma.
    """
    frames = []
    # For each json file in the repository path
    for file_path in glob.glob('%s/*.json' % path):
        article = pd.read_json(file_path, typ='series')
        try:
            article = pd.Series({'id':article['id_article'], 'source':article['newspaper'],
                                 'theme':article['theme'], 'title':article['title'],
                                 'list_lemma':article['content']['list_lemma']
                                 })
            article = article.to_frame('index').transpose()
            frames.append(article)
        except:
            # Do nothing
            pass
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
    sources = ['Le Monde', 'Le Figaro', 'Liberation', 'Nouvel Obs', 'Telerama',
               'Futura Sciences']
    # Let's recode each source one by one
    for source, source_dict in zip(sources, all_dicts):
        source_df = df[df['source'] == source]
        # Recode categories from the source
        source_df['theme'] = source_df['theme'].map(source_dict)
        # Concatenate with other sources in a single Dataframe
        df_recoded = pd.concat([df_recoded, source_df])
    df_recoded['theme'] = df_recoded['theme'].fillna('delete')
    #df_recoded = df_recoded[df_recoded['theme'] != 'delete']
    df_recoded['list_lemma'] = df_recoded['list_lemma'].map(lambda x: ' '.join(x))
    df.reset_index(drop=True, inplace=True)
    return df_recoded