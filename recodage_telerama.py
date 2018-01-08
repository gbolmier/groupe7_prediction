import pandas as pd
import glob


def import_data(folder):
    frames = []
    for file_path in glob.glob('%s/*.json' % path):
        article = pd.read_json(file_path, typ='series').to_frame('index').transpose()
        frames.append(article)
    df = pd.concat(frames)
    df.sort_values(by=['theme'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

path = '/home/sidu1/Documents/Ecole/SID/L3/Stage L3/text_classification/articles/telerama'
df = import_data(path)

# print themes labels
print(set(df['theme'].values))

# print article from a category
print(df['body'][df['theme'] == 'cinema'].values[0:2]) # print les 2 premiers articles

dict_telerama = {
        'livre':'Culture',
        'cinema':'Culture',
        'musique':'Culture',
        'series tv':'Culture',
        'radio':'Culture',
        'sortir':'France',
        'television':'Culture',
        'medias':'Culture',
        'monde':'International',
        'scenes':'Culture',
        'idees':'delete',
        'enfants':'delete'
        }

# Recode categories
df['new_cat'] = df['theme'].map(dict_telerama)