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

path = '/home/sidu1/Documents/Projet inter-promo 2018/target_press_article/telerama'
df = import_data(path)

# print themes labels
print(set(df['theme'].values))

# print article from a category
#print(df['body'][df['theme'] == 'cinema'].values[0:2]) # print les 2 premiers articles

dict_telerama = {
        'livre':'arts et culture',
        'cinema':'arts et culture',
        'musique':'arts et culture',
        'series tv':'arts et culture',
        'radio':'arts et culture',
        'sortir':'france',
        'television':'arts et culture',
        'medias':'arts et culture',
        'monde':'international',
        'scenes':'arts et culture',
        'idees':'delete',
        'enfants':'delete'
        }

# Recode categories
#df['new_cat'] = df['theme'].map(dict_telerama)