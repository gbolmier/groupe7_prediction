# -*- coding: utf-8 -*-
# group 7

import pandas as pd
import pickle
import glob


def import_data(recoded=False):
    """
    Take in parameter if we want to recode the themes and return data we need
    (id, source, theme, title, list_lemma, theme_recoded) in a pandas dataframe.
    """
    frames = []
    for file_path in glob.glob('../../../../data/data_group5/*.json'): # mettre le vrai chemin
        article = pd.read_json(file_path, typ='series')
        # Sometimes there are errors when parsing some articles, so we need to
        # prevent it with a try/except block
        try:
            article = pd.Series({'id':article['title'], 'source':article['newspaper'], # 'id':'id_article'
                                 'theme':article['theme'], 'title':article['title'],
                                 'list_lemma':article['content']['list_lemma']
                                 })
            article = article.to_frame().transpose()
            frames.append(article)
        except:
            # Do nothing
            pass
    df = pd.concat(frames)
    df.reset_index(drop=True, inplace=True)
    # Finally recode the categories if desired
    if recoded:
        # Load recoding dictionaries
        all_dicts = pickle.load(open('../get_data/g7_all_dicts', 'rb'))
        sources = ['Le Monde', 'Le Figaro', 'Liberation', 'Nouvel Obs', 'Telerama',
                   'Futura Sciences']
        df['theme_recoded'] = 'delete'
        # Recode each source in the list of sources
        for source,  source_dict in zip(sources, all_dicts):
            mask = df['source'] == source
            df.loc[mask, 'theme_recoded'] = df.loc[mask, 'theme'].map(source_dict)
        df['theme_recoded'] = df['theme_recoded'].fillna('delete')
    return df