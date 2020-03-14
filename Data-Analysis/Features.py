import pandas as pd

df = pd.DataFrame({
  'T1': [10, 15, 8],
  'T2': [25, 27, 25],
  'T3': [16, 15, 10]})

print(df.sum())
# T1    33
# T2    77
# T3    41
# dtype: int64
print(df.sum(axis=1))
# 0    51
# 1    57
# 2    43
# dtype: int64
print(df.mean())
# T1    11.000000
# T2    25.666667
# T3    13.666667
# dtype: float64
print(df.mean(axis=1))
# 0    17.000000
# 1    19.000000
# 2    14.333333
# dtype: float64

#multiply (a simple constant can be the argument)

print(df.multiply([1000, 2, 3]))
#       T1  T2  T3
# 0  10000  50  48
# 1  15000  54  45
# 2   8000  50  30
print(df.multiply([1000, 2, 3], axis=0))
#       T1     T2     T3
# 0  10000  25000  16000
# 1     30     54     30
# 2     24     75     30