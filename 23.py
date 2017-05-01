import numpy as np
import random

while True:
    b = 20
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(150, 300)
    v = sum(arr) / b
    f = 0
    for i in arr:
        if i < v:
            f += i
    print(arr)
    print(v)
    print(f)
    break