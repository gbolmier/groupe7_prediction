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

<<<<<<< Updated upstream:recoding_futurasciences.py
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
=======
path = './lemonde'
df = import_data(path)

# print themes labels
#print(set(df['theme'].values))


dicoThemes = {     
 'actualite medias': 'delete',
 'addictions' : 'sante',
 'affaire de la sextape de valbuena' : 'sport',
 'afrique' : 'international',
 'ameriques' : 'international',
 'architecture' : 'delete',
 'argent' : 'economie',
 'arts' : 'culture',
 'asie pacifique' : 'international',
 'attentat de manchester' : 'international',
 'auto moto' : 'sport',
 'bac lycee' : 'culture',
 'bande dessinee' : 'culture',
 'basket' : 'sport',
 'big browser' : 'science/high-tech',
 'campus' : 'culture',
 'cinema' : 'culture',
 'climat' : 'science/high-tech',
 'cosmos' : 'science/high-tech',
 'culture' : 'culture',
 'cyclisme' : 'sport',
 'disparitions' : 'delete',
 'djihad online' : 'international',
 'donald trump' : 'international',
 'economie' : 'economie',
 'economie francaise' : 'economie',
 'education' : 'culture',
 'elections legislatives 2017' : 'france',
 'emploi' : 'economie',
 'energies' : 'science/high-tech',
 'entreprises' : 'economie',
 'europe' : 'international',
 'fashion week' : 'culture',
 'femmes a part' : 'delete',
 'football' : 'sport',
 'formule 1' : 'sport',
 'gouvernement philippe' : 'france',
 'handball' : 'sport',
 'idees' : 'culture',
 'immigration et diversite' : 'international',
 'international' : 'international',
 'la foire du drone' : 'delete',
 'la republique en marche' : 'france',
 'ligue 1' : 'sport',
 'ligue des champions' : 'sport',
 'livres' : 'culture',
 'm actu' : 'delete',
 'm beaute' : 'sante',
 'm design deco' : 'delete',
 'm gastronomie' : 'culture',
 'm gastronomie le lieu' : 'culture',
 'm horlogerie joaillerie' : 'delete',
 'm le mag' : 'international',
 'm mode' : 'culture',
 'm mode business of fashion' : 'delete',
 'm moyen format' : 'delete',
 'm perso' : 'delete',
 'm styles' : 'delete',
 'm voiture' : 'sport',
 'm voiture banc d essai' : 'sport',
 'm voyage' : 'delete',
 'm voyage le lieu' : 'delete',
 'moyen orient irak' : 'international',
 'musiques' : 'culture',
 'o21' : 'delete',
 'paleontologie' : 'culture',
 'pixels' : 'science/high-tech',
 'planete' : 'international',
 'police justice' : 'delete',
 'politique' : 'culture',
 'pollution' : 'sante',
 'prix nobel' : 'science/high-tech',
 'proche orient' : 'international',
 'referendum sur le brexit' : 'international',
 'roland garros' : 'sport',
 'rugby' : 'sport',
 'sante' : 'sante',
 'scenes' : 'culture',
 'sciences' : 'science/high-tech',
 'smart cities' : 'science/high-tech',
 'societe' : 'culture',
 'sport' : 'sport',
 'sports de combat' : 'sport',
 'sports us' : 'sport',
 'syrie' : 'international',
 'tant de temps' : 'delete',
 'televisions radio' : 'culture',
 'tennis' : 'sport',
 'top 14' : 'sport',
 'universites' : 'science/high-tech',
 'vins' : 'culture'}


# Recode categories
df['new_cat'] = df['theme'].map(dicoThemes)

# Json with new cats
df.to_json('lemonde_new_cat.json', orient = 'index')
>>>>>>> Stashed changes:recodage_telerama.py
