import numpy as np

A =np.array([[1,2,3],[4,5,6]])
x = np.array([1,2,3])

print(A.shape)  # 输出: (2, 3)
print(x.shape)  # 输出: (3,)
result = A @ x
print(result)  # 输出: [14 32]


x1 = np.array([[1,2,3],[4,5,6]])
print(x1.shape)  # 输出: (2, 3)
result1 = A @ x1    
print(result1)  