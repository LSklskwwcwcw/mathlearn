import numpy as np

a1,b1 = 100,101
res1 = np.isclose(a1,b1,rtol=1e-2,atol=0)

""" ∣a−b∣≤atol+rtol×∣b∣ """

a2,b2 = 0.002,0.001
res2 = np.isclose(a2,b2,rtol=1e-2,atol=0)

print(f"第一组 (100 vs 101) 判定结果: {res1}")
print(f"第二组 (0.001 vs 0.002) 判定结果: {res2}")