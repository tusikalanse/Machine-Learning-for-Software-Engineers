import pandas as pd

df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'bettsmo01'],
  'yearID': [2016, 2016, 2016, 2016, 2015],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'BOS'],
  'HR': [31, 39, 43, 38, 18]})

sort = df.sort_values(['yearID', 'HR'],
                       ascending=[True, False])
print(sort)
#    HR   playerID teamID  yearID
# 4  18  bettsmo01    BOS    2015
# 2  43   cruzne02    SEA    2016
# 1  39   canoro01    SEA    2016
# 3  38  ortizda01    BOS    2016
# 0  31  bettsmo01    BOS    2016
