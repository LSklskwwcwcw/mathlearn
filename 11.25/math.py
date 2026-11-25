import matplotlib.pyplot as plt
import numpy  as np
import math

P = np.array([1, 2, 3, 4, 5, 6])
rng = np.random.default_rng(seed=42)
repeats = 1000
n_values = [1, 5, 20, 50]

mu = 3.5
sigma = math.sqrt(35/12)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()
for n,ax in zip(n_values,axes):
    means_list = []
    for i in range(repeats):
        sample = rng.choice(P,size=n,replace=True)
        means_list.append(np.mean(sample))

    ax.hist(means_list, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black')
    ax.set_title(f"样本量 n={n}")
    ax.set_xlabel("样本均值")
    ax.set_ylabel("概率密度")

plt.tight_layout()
plt.show()