import pandas as pd

#direct index: each column can be a key
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]}, index=['r1', 'r2'])
col1 = df['c1']
print(col1)
print(type(col1))
# r1    1
# r2    2
# Name: c1, dtype: int64
# <class 'pandas.core.series.Series'>

col1_df = df[['c1']]
print(col1_df)
print(type(col1_df))
#     c1
# r1   1
# r2   2
# <class 'pandas.core.frame.DataFrame'>

#retrieve rows based on slices
print(df[0:1]) #1 is exclusive
#     c1  c2  c3
# r1   1   3   5
print(df['r1':'r2']) #'r2' is inclusive
#     c1  c2  c3
# r1   1   3   5
# r2   2   4   6

#iloc / loc
df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])
                   
print(df.iloc[1])
# c1    2
# c2    5
# c3    8
# Name: r2, dtype: int64
print(df.iloc[[0, 2]])
#     c1  c2  c3
# r1   1   4   7
# r3   3   6   9
bool_list = [False, True, True]
print(df.iloc[bool_list])
#     c1  c2  c3
# r2   2   5   8
# r3   3   6   9

print(df.loc['r2'])
# c1    2
# c2    5
# c3    8
# Name: r2, dtype: int64

single_val = df.loc['r1', 'c2']
print(single_val) #4

print(df.loc[['r1', 'r3'], 'c2'])
# r1    4
# r3    6
# Name: c2, dtype: int64

df.loc[['r1', 'r3'], 'c2'] = 0
print(df)
#     c1  c2  c3
# r1   1   0   7
# r2   2   5   8
# r3   3   0   9