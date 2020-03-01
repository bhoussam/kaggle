import os

import pandas as pd
import tools.utils

DATADIR = os.path.abspath('data/french-ligue-1_zip/data')

df = pd.read_csv(os.path.join(DATADIR, 'season-0910_csv.csv'), sep=',', )

for file in os.listdir(DATADIR):
    if file.endswith('.csv'):
        if not file.endswith('0910_csv'):
            tmp = pd.read_csv(os.path.join(DATADIR, 'season-0910_csv.csv'), sep=',', )
            df = df.append(tmp)

print(df.dtypes)