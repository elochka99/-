import numpy as np
import random

while True:
    b = 5
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(-10, 10)
    print(arr)
    g = 1
    for i in arr:
        if i != 0:
            g *= i
    print(g)
    break