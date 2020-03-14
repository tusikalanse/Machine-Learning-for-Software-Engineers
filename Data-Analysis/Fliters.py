import pandas as pd

df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'bettsmo01'],
  'yearID': [2016, 2016, 2016, 2016, 2015],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'BOS'],
  'HR': [31, 39, 43, 38, 18]})

print(df['HR'] > 40)
# 0    False
# 1    False
# 2     True
# 3    False
# 4    False
# Name: HR, dtype: bool

print(df[df['HR'] > 40])
#    HR  playerID teamID  yearID
# 2  43  cruzne02    SEA    2016

##==, !=, <, >, <=, >=, isna, notna, isin

str_f1 = df['playerID'].str.startswith('c')
print(str_f1)
# 0    False
# 1     True
# 2     True
# 3    False
# 4    False
# Name: playerID, dtype: bool
##endswith, contains