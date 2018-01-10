#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import glob


def import_data(folder):
    frames = []
    sites = ['lemonde', 'lefigaro', 'futurasciences', 'liberation', 'telerama', 'nouvelobs']
    for site in sites:
        for file_path in glob.glob('%s/%s/*.json' % (path, site)):
            article = pd.read_json(file_path, typ='series').to_frame('index').transpose()
            frames.append(article)
    df = pd.concat(frames)
    df.sort_values(by=['theme'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

path = '/home/sidu1/Documents/Projet inter-promo 2018/target_press_article/'
df = import_data(path)

