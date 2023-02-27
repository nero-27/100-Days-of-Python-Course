import pandas as pd
import numpy as np

df = pd.read_csv('squirrel_data_2018.csv')

cinnamon_squirrels_count = len(df[df['Primary Fur Color'] == 'Cinnamon'])
gray_squirrels_count = len(df[df['Primary Fur Color'] == 'Gray'])
black_squirrels_count = len(df[df['Primary Fur Color'] == 'Black'])
print(cinnamon_squirrels_count, gray_squirrels_count, black_squirrels_count)
data_dict = {
    'fur_color': ['Gray', 'Cinnamon', 'Black'],
    'count': [2473, 392, 103],
}

new_df = pd.DataFrame(data_dict)
new_df.to_csv('squirrels_data_summary.csv')
