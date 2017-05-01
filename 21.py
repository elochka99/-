import numpy as np
import random

while True:
    v = float(input('ffff'))
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.uniform(50, 100)
    g = 1
    for i in arr:
        if i < v:
            g *= i
    print(arr)
    print(g)
    break