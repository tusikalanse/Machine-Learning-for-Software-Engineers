import xgboost as xgb
import numpy as np

data = np.array([
  [1.2, 3.3, 1.4],
  [5.1, 2.2, 6.6]])

labels = np.array([0, 1])

dtrain = xgb.DMatrix(data, label=labels)

params = {
  'max_depth': 0,
  'objective': 'binary:logistic'
}
bst = xgb.train(params, dtrain)  

eval_data = np.array([
    [1.3, 3.8, 1.3],
    [6.3, 1.5, 4.6]
])

eval_labels = np.array([0, 1])

print(bst.eval(xgb.DMatrix(eval_data, label=eval_labels)))
# [0]     eval-error:0.500000

new_data = np.array([
    [6.2, 3.5, 1.4],
    [2.3, 6.5, 1.8],
    [8.5, 1.6, 7.4]
])

print(bst.predict(xgb.DMatrix(new_data)))
# [0.5 0.5 0.5] return probility