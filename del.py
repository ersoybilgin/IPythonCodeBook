import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

switches = {'pandas': True, 'numpy': False, 'html': False,
            'numba': False, 'replace': False, 'numexpr': False,
            'ctypes': False, 'cython': False}

print('\n', switches, '\n')

# ------------ Pandas -------------------
if switches['pandas']:
    print('\n ---- STARTING Pandas:  \n')

    url = "http://donnees.ville.montreal.qc.ca/dataset/f170fecc-18db" \
          "-44bc-b4fe-5b0b6d2c7297/resource/ec12447d-6b2a-45d0-b0e7" \
          "-fd69c382e368/download/2013.csv"

    df = pd.read_csv(url, index_col='Date', parse_dates=True,
                     dayfirst=True)
    print(df.head(2), "\n")
    print(df.describe())

    df[['Mais2', 'PierDup']].plot(figsize=(16, 12), style=['-', '--'])
    plt.ylim(0)

    df[['Berri1', 'CSC', 'Mais1', 'Mais2', 'Parc', 'PierDup',
        'Rachel1', 'Totem_Laurier']].plot(figsize=(16, 12),
                                          style=['-', '--'])
    plt.ylim(0)

    pd.rolling_mean(df[['Berri1', 'CSC', 'Mais1', 'Mais2', 'Parc',
                        'PierDup', 'Rachel1', 'Totem_Laurier']],
                    28).dropna().plot(figsize=(16, 12),
                                      style=['-', '--'])
    plt.ylim(0)

    days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                     'Friday', 'Saturday', 'Sunday'])
    df['Weekday'] = days[df.index.weekday]

    df_week = df.groupby('Weekday').sum()
    df_week.ix[days].plot(lw=3, figsize=(12, 8))
    plt.ylim(0)

    months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    df['Month'] = months[df.index.month - 1]

    df_month = df.groupby('Month').sum()
    df_month.ix[months].plot(lw=3, figsize=(12, 8))
    plt.ylim(0)

    df_month_week = df.groupby(['Month', 'Weekday']).sum()
else:
    print('\n ---- Skipping Pandas:  \n')