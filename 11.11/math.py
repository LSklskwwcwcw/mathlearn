import numpy as np
import math

A = np.array([[1,2,3],[4,5,6]])
print(A.shape)

B = np.array([[1,2],[3,4],[5,6]])
print(B.shape)

result = A @ B
print(result)
print(result.shape)


str_sci = "1.23e-4"
num_sci = float(str_sci)
print(num_sci)

str_overflow = "1e400"
print(float(str_overflow))

nan_val = float("nan")
inf_val = float("inf")
print(nan_val)
print(inf_val)

print(type(nan_val))
print(type(inf_val))

print(math.isfinite(1.5e3))
print(math.isfinite(float("inf")))
print(math.isfinite(float("nan")))