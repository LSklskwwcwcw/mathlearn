import numpy as np

x = np.array([8,10,10,12,15])

means = np.mean(x)
print(means)

print(np.var(x,ddof=0))
print(np.var(x,ddof=1))


x[-1] = 30
print(np.mean(x))
print(np.var(x,ddof=0))
print(np.var(x,ddof=1))