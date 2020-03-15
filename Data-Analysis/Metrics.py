import pandas as pd

df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]}, index=['r1', 'r2'])
print(df.describe())
#              c1        c2        c3
# count  2.000000  2.000000  2.000000
# mean   1.500000  3.500000  5.500000
# std    0.707107  0.707107  0.707107
# min    1.000000  3.000000  5.000000
# 25%    1.250000  3.250000  5.250000
# 50%    1.500000  3.500000  5.500000
# 75%    1.750000  3.750000  5.750000
# max    2.000000  4.000000  6.000000

print(df['c1'].value_counts()) #ascending=?, normalize=?
# 2    1
# 1    1
# Name: c1, dtype: int64

print(df['c1'].unique())
#[1 2]