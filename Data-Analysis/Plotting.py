import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'bettsmo01'],
  'yearID': [2016, 2016, 2016, 2016, 2015],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'BOS'],
  'HR': [31, 39, 43, 38, 18]})

df.plot()
plt.show()
plt.title('HR vs. Year')
plt.xlabel('Year')
plt.ylabel('HR Count')

plt.savefig('example.png')