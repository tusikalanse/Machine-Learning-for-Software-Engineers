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

#contact
df1 = pd.DataFrame({'c1':[1,2], 'c2':[3,4]},
                   index=['r1','r2'])
df2 = pd.DataFrame({'c1':[5,6], 'c2':[7,8]},
                   index=['r1','r2'])
df3 = pd.DataFrame({'c1':[5,6], 'c2':[7,8]})

concat = pd.concat([df1, df2], axis=1)
print(concat)
#     c1  c2  c1  c2
# r1   1   3   5   7
# r2   2   4   6   8

concat = pd.concat([df1, df3])
print(concat)
#     c1  c2
# r1   1   3
# r2   2   4
# 0    5   7
# 1    6   8

concat = pd.concat([df1, df3], axis=1) #match labels
print(concat)
#      c1   c2   c1   c2
# r1  1.0  3.0  NaN  NaN
# r2  2.0  4.0  NaN  NaN
# 0   NaN  NaN  5.0  7.0
# 1   NaN  NaN  6.0  8.0


#merge
#the rows with same common cloumns will be merged if no keyword arguments given
df1 = pd.DataFrame({'name' : ['zxj', 'hyc', 'wrj'],
                    'sex' : ['M', 'M', 'M'],
                    'money' : [100, 100000, 100]})
df2 = pd.DataFrame({'name' : ['zxj', 'hyc', 'wrj'],
                    'sex' : ['M', 'M', 'F'],
                    'year' : [1000, 1000, 100]})
print(pd.merge(df1, df2))
#     money name sex  year
# 0     100  zxj   M  1000
# 1  100000  hyc   M  1000