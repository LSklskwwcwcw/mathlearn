import numpy as np

print(np.isclose(0.1 + 0.2, 0.3))
print(0.1 + 0.2 == 0.3)


""" 
差 5.55e-17。== 比较的是这两个数是不是完全一样，不是"差不多"——所以 False。

np.isclose 问的是"差距是否小到可以忽略"——所以 True。 """