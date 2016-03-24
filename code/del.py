import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

switches = {'pandas': False, 'numpy': True, 'html': False,
            'numba': True, 'replace': False, 'numexpr': False,
            'ctypes': False, 'cython': False}

print('\n', switches, '\n')

print('\nExamples for these packages will be run: \n')

for i, packageName in enumerate(list(key for key, value in
                                   switches.items() if value == True)):
    print('    {0}. {1}'.format(i+1, packageName))



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


# ------------ NumPy -------------------
if switches['numpy']:
    print('\n ---- STARTING NumPy:  \n')

    import timeit

    n = 1000000

    x = [random.random() for _ in range(n)]
    y = [random.random() for _ in range(n)]

    xa = np.array(x)
    ya = np.array(y)

    nmbRepeats = 10

    t1 = timeit.timeit('[x[i] + y[i] for i in range(n)]',
                       setup="from __main__ import x, y, n", number=nmbRepeats)  # pure Python
    print('\n ---- Timer 1.1, sum two arrays in pure Python: time = {'
          '0:1.3f}'.format(t1))
    t2 = timeit.timeit('xa + ya', setup="from __main__ import xa, ya",
                       number=nmbRepeats)  # NumPy
    print(
        '\n ---- Timer 1.2, sum two arrays in NumPy: time = {'
        '0:1.3f}'.format(
            t2))
    print('\n   ratio = {0:1.0f}'.format(t1 / t2))

    t1 = timeit.timeit('sum(x)', setup="from __main__ import x",
                       number=nmbRepeats)  # pure Python
    print('\n ---- Timer 2.1, sum all values of an array in pure '
          'Python: time = {0:1.3f}'.format(t1))
    t2 = timeit.timeit('np.sum(xa)',
                       setup="from __main__ import np, xa",
                       number=nmbRepeats)  # NumPy
    print('\n ---- Timer 2.2, sum all values of an array in NumPy: '
          'time = {0:1.3f}'.format(t2))
    print('\n   ratio = {0:1.0f}'.format(t1 / t2))

    t1 = timeit.timeit('[abs(x[i] - y[j]) for i in range(1000) for j '
                       'in range(1000)]',
                       setup="from __main__ import x, y",
                       number=nmbRepeats)
    print('\n ---- Timer 3.1, absolute distance between all items of '
          'two arrays in pure Python: time = {0:1.3f}'.format(t1))
    t2 = timeit.timeit('np.abs(xa[:1000, None] - ya[:1000])',
                       setup="from __main__ import np, xa, ya",
                       number=nmbRepeats)
    print('\n ---- Timer 3.2, absolute distance between all items of '
          'two arrays in NumPy: time = {0:1.3f}'.format(t2))
    print('\n   ratio = {0:1.0f}'.format(t1 / t2))
else:
    print('\n ---- Skipping NumPy:  \n')

