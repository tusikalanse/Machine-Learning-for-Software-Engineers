import pandas as pd

#1-D array
series = pd.Series(5)
print(series)
#0    5
#dtype: int64

#index (any hashable type is OK)
series2 = pd.Series([1, 2, 3], index=['a', 0.4, 2])
print(series2)
#a    1
#0.4  2
#2    3
#dtype: int64

#another way to set index : Dictionary input
series3 = pd.Series({'a' : 1, 0.4 : 2, 2 : 3})
print(series2.equals(series3)) #True