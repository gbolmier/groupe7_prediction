# -*- coding: utf-8 -*-
# group 7

import pickle


dict_lemonde = {
        'actualite medias': 'france',
        'addictions': 'sante',
        'affaire baupin': 'france',
        'affaire de la sextape de valbuena': 'france',
        'affaire penelope fillon': 'france',
        'afrique': 'international',
        'al qaida': 'international',
        'ameriques': 'international',
        'archeologie': 'arts_et_culture',
        'architecture': 'arts_et_culture',
        'archives': 'delete',
        'argent': 'economie',
        'arts': 'arts_et_culture',
        'asie pacifique': 'international',
        'athletisme': 'sports',
        'attaques a paris': 'france',
        'attentat de manchester': 'international',
        'auto moto': 'sports',
        'automobile': 'sports',
        'bac lycee': 'france',
        'bande dessinee': 'arts_et_culture',
        'basket': 'sports',
        'big browser': 'international',
        'biodiversite': 'sciences_high_tech',
        'bleds a part': 'france',
        'brevet college': 'france',
        'campus': 'arts_et_culture',
        'chronique des communs': 'delete',
        'cinema': 'arts_et_culture',
        'citynnovation': 'sciences_high_tech',
        'climat': 'france',
        'collection musee ideal': 'arts_et_culture',
        'collection mythologie': 'arts_et_culture',
        'commerce gestion': 'economie',
        'concours': 'delete',
        'conferences climat': 'france',
        'corse': 'france',
        'cosmos': 'international',
        'cotecourscotesjardins': 'arts_et_culture',
        'culture': 'arts_et_culture',
        'cyclisme': 'sports',
        'decryptages': 'delete',
        'demographie': 'international',
        'disparitions': 'arts_et_culture',
        'djihad online': 'international',
        'donald trump': 'international',
        'droit sciences po': 'sciences_high_tech',
        'economie': 'economie',
        'economie francaise': 'economie',
        'economie mondiale': 'economie',
        'education': 'arts_et_culture',
        'election presidentielle 2017': 'france',
        'elections': 'france',
        'elections americaines': 'international',
        'elections legislatives 2017': 'france',
        'elections senatoriales': 'france',
        'emmanuel macron': 'france',
        'emploi': 'france',
        'en bref': 'delete',
        'energies': 'france',
        'entre les lignes': 'delete',
        'entreprises': 'economie',
        'europe': 'international',
        'evasion fiscale': 'economie',
        'fashion week': 'arts_et_culture',
        'femmes a part': 'delete',
        'festival': 'arts_et_culture',
        'festival de cannes': 'arts_et_culture',
        'fin de vie': 'delete',
        'financement de la sante': 'economie',
        'football': 'sports',
        'formule 1': 'sports',
        'golf': 'sports',
        'gouvernement philippe': 'france',
        'gymnastique': 'sports',
        'handball': 'sports',
        'hillary clinton': 'international',
        'idees': 'arts_et_culture',
        'immigration et diversite': 'international',
        'immobilier': 'economie',
        'international': 'international',
        'jeux olympiques pyeongchang 2018': 'sports',
        'jeux olympiques rio 2016': 'sports',
        'judo': 'sports',
        'la foire du drone': 'sciences_high_tech',
        'la france insoumise': 'france',
        'la matinale': 'france',
        'la republique en marche': 'france',
        'le blog du decodex': 'delete',
        'les decodeurs': 'arts_et_culture',
        'les enfants akira': 'arts_et_culture',
        'les nouveaux arrivants': 'international',
        'ligue 1': 'sports',
        'ligue des champions': 'sports',
        'livres': 'arts_et_culture',
        'logement': 'economie',
        'logiciel de racket wannacry': 'sciences_high_tech',
        'lycee': 'arts_et_culture',
        'm actu': 'france',
        'm actu chroniques': 'france',
        'm beaute': 'arts_et_culture',
        'm design deco': 'arts_et_culture',
        'm gastronomie': 'arts_et_culture',
        'm gastronomie le lieu': 'arts_et_culture',
        'm gens portrait': 'arts_et_culture',
        'm horlogerie joaillerie': 'arts_et_culture',
        'm le mag': 'arts_et_culture',
        'm mode': 'arts_et_culture',
        'm mode business of fashion': 'arts_et_culture',
        'm moyen format': 'arts_et_culture',
        'm perso': 'delete',
        'm styles': 'arts_et_culture',
        'm voiture': 'sports',
        'm voiture banc d essai': 'sports',
        'm voyage': 'arts_et_culture',
        'm voyage le lieu': 'arts_et_culture',
        'marches financiers': 'economie',
        'medecine': 'sante',
        'meurtres de policiers a magnanville': 'france',
        'mondial 2018': 'sports',
        'mort de france gall': 'arts_et_culture',
        'mort de simone veil': 'arts_et_culture',
        'moyen orient irak': 'international',
        'musiques': 'arts_et_culture',
        'nutrition': 'sante',
        'o21': 'delete',
        'one planet summit': 'delete',
        'organisations internationales': 'international',
        'paleontologie': 'sciences_high_tech',
        'paradise papers': 'international',
        'partir a l etranger': 'arts_et_culture',
        'photo': 'arts_et_culture',
        'pixels': 'sciences_high_tech',
        'planete': 'sciences_high_tech',
        'police justice': 'france',
        'politique': 'france',
        'pollution': 'france',
        'prix nobel': 'international',
        'proche orient': 'international',
        'referendum sur le brexit': 'international',
        'religions': 'france',
        'roland garros': 'sports',
        'rugby': 'sports',
        'sante': 'sante',
        'scenes': 'arts_et_culture',
        'sciences': 'sciences_high_tech',
        'securite sanitaire': 'sante',
        'ski': 'sports',
        'smart cities': 'sciences_high_tech',
        'societe': 'france',
        'sport': 'sports',
        'sport et societe': 'sports',
        'sports de combat': 'sports',
        'sports de glisse': 'sports',
        'sports mecaniques': 'sports',
        'sports mecaniques formule 1': 'sports',
        'sports us': 'sports',
        'syrie': 'international',
        'tant de temps': 'delete',
        'technologies': 'sciences_high_tech',
        'televisions radio': 'arts_et_culture',
        'tempete harvey': 'international',
        'tennis': 'sports',
        'the rolling stones': 'arts_et_culture',
        'top 14': 'sports',
        'tour de france': 'sports',
        'universites': 'arts_et_culture',
        'vins': 'arts_et_culture',
        'violences policieres': 'france',
        'voile': 'sports',
        'volley': 'sports',
        'yemen': 'international'
        }

dict_lefigaro = {
        'vox': 'delete',
        'bd': 'arts_et_culture',
        'culture': 'arts_et_culture',
        'secteur': 'sciences_high_tech',
        'actualite france': 'france',
        'derives': 'sciences_high_tech',
        'emploi': 'economie',
        'langue francaise': 'arts_et_culture',
        'expertise': 'economie',
        'sortir paris': 'arts_et_culture',
        'equitation': 'sports',
        'devises matieres premieres': 'economie',
        'social': 'france',
        'sciences': 'sciences_high_tech',
        'cinema': 'arts_et_culture',
        'vie bureau': 'delete',
        'societes': 'economie',
        'jardin': 'arts_et_culture',
        'musique': 'arts_et_culture',
        'automobile': 'sports',
        'politique': 'france',
        'voyages': 'arts_et_culture',
        'flash eco': 'economie',
        'horlogerie': 'delete',
        'histoire': 'arts_et_culture',
        'arts expositions': 'arts_et_culture',
        'gastronomie': 'arts_et_culture',
        'retraite': 'economie',
        'conso': 'economie',
        'indices actions': 'economie',
        'international': 'international',
        'economie': 'economie',
        'theatre': 'arts_et_culture',
        'jeux video': 'sciences_high_tech',
        'mode homme': 'arts_et_culture',
        'lifestyle': 'arts_et_culture',
        'le scan sport': 'sports',
        'livres': 'arts_et_culture',
        'programme tv': 'arts_et_culture',
        'fonds trackers': 'economie',
        'entrepreneur': 'economie',
        'assurance': 'economie',
        'elections': 'france',
        'medias': 'delete',
        'conjoncture': 'economie',
        'article': 'economie'
        }

dict_liberation = {
        'planete': 'sciences_high_tech',
        'france': 'france',
        'sports': 'sports',
        'desintox': 'delete',
        'debats': 'delete',
        'elections presidentielle legislatives 2017': 'france',
        'futurs': 'delete',
        'une saison a la montagne': 'delete',
        'chroniques': 'delete',
        'redecouvrir athenes': 'arts_et_culture',
        'photographie': 'arts_et_culture',
        'sciences': 'sciences_high_tech',
        'evenements libe': 'delete',
        'voyage au coeur de lIA': 'sciences_high_tech',
        'politiques': 'france',
        'sous le soleil exactement': 'delete',
        'voyages': 'arts_et_culture',
        'checknews': 'delete',
        'saison en hiver': 'delete'
        }

dict_nouvelobs = {
        'monde': 'international',
        'sante': 'sante',
        'actualites': 'delete',
        'cinema': 'arts_et_culture',
        'sciences': 'sciences_high_tech',
        'voyage': 'arts_et_culture',
        'mode': 'arts_et_culture',
        'societe': 'france',
        'lifestyle': 'arts_et_culture',
        'notizie italiane': 'delete',
        'edito': 'delete',
        'sport': 'sports',
        'faits divers': 'france',
        'high tech': 'sciences_high_tech',
        'tech': 'sciences_high_tech',
        'food': 'arts_et_culture',
        'pop life': 'arts_et_culture',
        'l histoire du soir': 'delete',
        'planete': 'delete',
        'education': 'france',
        'design': 'arts_et_culture',
        'rue89': 'delete',
        'conso': 'economie',
        'politique': 'france',
        'bd': 'arts_et_culture',
        'jeux video': 'sciences_high_tech',
        'brexit': 'international',
        'presidentielle 2017': 'france',
        'documentaire': 'international',
        'documents': 'arts_et_culture',
        'idees': 'delete',
        'le grand oral': 'france',
        'justice': 'france',
        'culture': 'arts_et_culture',
        'l humeur de jerome garcin': 'international',
        'assises internationales du roman': 'arts_et_culture',
        'la selection teleobs': 'delete',
        'sur le sentier des prix': 'arts_et_culture',
        'voyages lointains': 'arts_et_culture',
        'critique': 'arts_et_culture',
        'theatre': 'arts_et_culture',
        'people': 'delete',
        'attentats terroristes a paris': 'france',
        'emotion canada': 'arts_et_culture',
        'series': 'arts_et_culture',
        'auto moto': 'sports',
        'info radio': 'arts_et_culture',
        'beaux livres': 'arts_et_culture',
        'faits divers': 'france',
        'read in the usa': 'international',
        'en partenariat avec books': 'arts_et_culture',
        'medias': 'delete',
        'musique': 'arts_et_culture',
        'l enquete de l obs': 'delete',
        'romans': 'arts_et_culture',
        'art design': 'arts_et_culture',
        'la selection teleobs': 'delete',
        'sur le sentier des prix': 'arts_et_culture',
        'chroniques': 'international',
        'voyages lointains': 'arts_et_culture',
        'theatre': 'arts_et_culture',
        'economie': 'economie',
        'editos et chroniques': 'international',
        'histoire': 'arts_et_culture',
        'le plus': 'delete',
        'les internets': 'delete',
        'photo': 'international',
        'tous feministes': 'france'
        }

dict_telerama = {
        'livre': 'arts_et_culture',
        'cinema': 'arts_et_culture',
        'musique': 'arts_et_culture',
        'series tv': 'arts_et_culture',
        'radio': 'arts_et_culture',
        'sortir': 'arts_et_culture',
        'television': 'arts_et_culture',
        'medias': 'delete',
        'monde': 'international',
        'scenes': 'arts_et_culture',
        'idees': 'delete',
        'enfants': 'delete',
        'festival de cannes': 'arts_et_culture'
        }

dict_futurasciences = {
        'tech': 'sciences_high_tech',
        'sciences': 'sciences_high_tech',
        'planete': 'sciences_high_tech',
        'sante': 'sante',
        'maison': 'sciences_high_tech'
        }

all_dicts = []
all_dicts.append(dict_lemonde)
all_dicts.append(dict_lefigaro)
all_dicts.append(dict_liberation)
all_dicts.append(dict_nouvelobs)
all_dicts.append(dict_telerama)
all_dicts.append(dict_futurasciences)

# Save our list of dictionnaries in a pickle file
pickle.dump(all_dicts, open('g7_all_dicts', 'wb'))
