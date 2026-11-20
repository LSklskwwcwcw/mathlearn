import math
import numpy as np

rng = np.random.default_rng(seed=42)

P = np.array([2,4,6,8])

simulation_times = [10,100,10000]


for n in simulation_times:
    sample_means = []
    for i in range(n):
        sample = rng.choice(P,size=2,replace=True)
        means = np.mean(sample)
        sample_means.append(means)

    mean_of_means = np.mean(sample_means)
    print(f"模拟 {n} 次时，样本均值的平均值为: {mean_of_means}")