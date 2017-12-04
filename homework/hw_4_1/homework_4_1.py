import os
import pandas as pd


DATA_DIR = r'.\names'


def top3_names(years):
    df = pd.DataFrame(columns=['name', 'number'])

    for year in years:
        file_name = os.path.join(DATA_DIR, f'yob{year}.txt')
        cur_df = pd.read_csv(file_name, header=None, names=['name', 'sex', 'number'])
        df = df.append(cur_df[['name', 'number']])

    df = df.groupby(['name']).aggregate(sum)
    df = df.sort_values('number', ascending=False)

    print('ТОП-3 популярных имен в указанные годы:', ', '.join(df.iloc[:3].index.values))


def count_dynamics(years):
    list_f = []
    list_m = []

    for year in years:
        file_name = os.path.join(DATA_DIR, f'yob{year}.txt')
        cur_df = pd.read_csv(file_name, header=None, names=['name', 'sex', 'number'])
        cur_df = cur_df[['sex', 'number']].groupby(['sex']).aggregate(sum)

        list_f.append(str(cur_df.loc['F'][0]))
        list_m.append(str(cur_df.loc['M'][0]))

    print('Динамика изменения количества женских имен: ', ', '.join(list_f))
    print('Динамика изменения количества мужских имен: ', ', '.join(list_m))


top3_names(['1880', '1881', '1882'])
count_dynamics(['1880', '1881', '1882'])