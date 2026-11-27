import numpy as np
import math


P = np.array([1, 2, 3, 4, 5, 6])
rng = np.random.default_rng(seed=42)
repeats = 10000
n_values = [25, 100]
mu = 3.5
sigma = math.sqrt(35/12)

z_val = 1.96


for n in n_values:
    counts = 0
    weight = 0
    E = z_val * (sigma / math.sqrt(n))
    for i in range(repeats):
        x_bar = np.mean(rng.choice(P,size=n,replace=True))
        down = x_bar - E
        up= x_bar + E
        weight += (up - down)
        if mu >= down and mu <= up:
            counts+=1
    coverage = counts / repeats
    avg_width = weight / repeats
    print(f"样本量 n={n}: 实际覆盖率={coverage:.4f}, 平均区间宽度={avg_width:.4f}")