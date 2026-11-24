import numpy as np
import math

P =np.array([2,4,6,8])
rng = np.random.default_rng(seed=42)
repeats = 1000

sigma = np.std(P) 

sample_sizes = [2, 5, 20, 100]
for n in sample_sizes:
    list1 = []
    for i in range(repeats):
        means = np.mean(rng.choice(P,size=n,replace=True))
        list1.append(means)
    result1 = np.std(list1)
    result2 = sigma / math.sqrt(n)
    absolute_error = abs(result1 - result2)

    print(f"样本量 n={n:3}: 模拟标准误={result1:.4f}, 理论标准误={result2:.4f}, 绝对误差={absolute_error:.4f}")
