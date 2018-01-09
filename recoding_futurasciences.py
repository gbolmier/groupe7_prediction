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

path = '/home/sidu1/Documents/Projet inter-promo 2018/target_press_article/futurasciences'
df = import_data(path)

# print themes labels
print(set(df['theme'].values))

# print article from a category
#print(df['body'][df['theme'] == 'maison'].values[0:2]) # print les 2 premiers articles

dict_futurascience= {
        'tech':'sciences/high-tech',
        'sciences':'sciences/high-tech',
        'planete':'sciences/high-tech',
        'sante':'sante',
        'maison':'sciences/high-tech'
        }

# Recode categories
#df['new_cat'] = df['theme'].map(dict_futurasciences)