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

bst.save_model("model.bin")
# [0.5 0.5 0.5] return probility