import pandas as pd
import numpy as np

df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'bettsmo01'],
  'yearID': [2016, 2016, 2016, 2016, 2015],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'BOS'],
  'HR': [31, 39, 43, 38, 18]})

dm = pd.get_dummies(df)

print(dm)
#    HR  yearID  playerID_bettsmo01  playerID_canoro01  playerID_cruzne02  \
# 0  31    2016                   1                  0                  0   
# 1  39    2016                   0                  1                  0   
# 2  43    2016                   0                  0                  1   
# 3  38    2016                   0                  0                  0   
# 4  18    2015                   1                  0                  0   

#    playerID_ortizda01  teamID_BOS  teamID_SEA  
# 0                   0           1           0  
# 1                   0           0           1  
# 2                   0           0           1  
# 3                   1           1           0  
# 4                   0           1           0  

n_mat = dm.values

print(n_mat)
# [[  31 2016    1    0    0    0    1    0]
#  [  39 2016    0    1    0    0    0    1]
#  [  43 2016    0    0    1    0    0    1]
#  [  38 2016    0    0    0    1    1    0]
#  [  18 2015    1    0    0    0    1    0]]