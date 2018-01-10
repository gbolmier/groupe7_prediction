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

<<<<<<< Updated upstream:recoding_telerama.py
path = '/home/sidu1/Documents/Projet inter-promo 2018/target_press_article/telerama'
=======
path = "C:/Users/pouch/Desktop/articles/lefigaro"
>>>>>>> Stashed changes:recodage_telerama.py
df = import_data(path)

# print themes labels
print(set(df['theme'].values))

# print article from a category
<<<<<<< Updated upstream:recoding_telerama.py
#print(df['body'][df['theme'] == 'cinema'].values[0:2]) # print les 2 premiers articles
=======
<<<<<<< Updated upstream
print(df['body'][df['theme'] == 'cinema'].values[0:2]) # print les 2 premiers articles
>>>>>>> Stashed changes:recodage_telerama.py

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
<<<<<<< Updated upstream:recoding_telerama.py
#df['new_cat'] = df['theme'].map(dict_telerama)
=======
df['new_cat'] = df['theme'].map(dict_telerama)
=======
#print(df['body'][df['theme'] == 'secteur'].values)
>>>>>>> Stashed changes
>>>>>>> Stashed changes:recodage_telerama.py
