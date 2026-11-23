import numpy as np

sample_sizes = [2, 5, 20, 100]
repeats = 10000
rng = np.random.default_rng(seed=42)
P = np.array([2,4,6,8])


for n in sample_sizes:
    list = []
    for i in range(1,repeats + 1):
        sample = rng.choice(P,size=n,replace=True)
        means = np.mean(sample)
        list.append(means)
    finalresult = np.std(list)

    print(f"第{n}次时，标准差为{finalresult}")