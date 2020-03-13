import pandas as pd

#2-D array
df = pd.DataFrame()
print('{}\n'.format(df))
# Empty DataFrame
# Columns: []
# Index: []

df = pd.DataFrame([[5,6]])
print('{}\n'.format(df))
#    0  1
# 0  5  6

df = pd.DataFrame([[5, 6], [1, 3]],
                  index=['r1', 'r2'],
                  columns=['c1', 'c2'])
print('{}\n'.format(df))
    # c1  c2
# r1   5   6
# r2   1   3
#the DataFrame takes the dictionary's keys as its column labels.

#upcast (occurs on a per-column basis)
upcast = pd.DataFrame([[5, 6], [1.2, 3]])
print(upcast)
# Datatypes of each column
print(upcast.dtypes)
#      0  1
# 0  5.0  6
# 1  1.2  3
# 0    float64
# 1      int64
# dtype: object

#append rows (Series or DataFrame)
df = pd.DataFrame([[5, 6], [1.2, 3]])
df2 = df.append(df)
print(df2)
#      0  1
# 0  5.0  6
# 1  1.2  3
# 0  5.0  6
# 1  1.2  3

#drop: drop rows or cloumns (using labels=''&axis='' or index='', cloumns='')