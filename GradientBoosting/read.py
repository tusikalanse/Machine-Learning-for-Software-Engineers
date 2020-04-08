import xgboost as xgb
import numpy as np
new_bst = xgb.Booster()

new_bst.load_model("model.bin")

new_data = np.array([
    [6.2, 3.5, 1.4],
    [2.3, 6.5, 1.8],
    [8.5, 1.6, 7.4]
])

print(new_bst.predict(xgb.DMatrix(new_data)))
# [0.5 0.5 0.5] return probility