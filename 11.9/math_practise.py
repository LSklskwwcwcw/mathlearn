import numpy as np

matrix = np.array(
    [[1,2],
     [3,4]]
)

vector = np.array([5,6])


result = matrix @ vector
print(matrix.shape)
print(vector.shape)  # 输出: [17 39]
print(result)  # 输出: [17 39]
print(result.shape)  # 输出: (2,)
