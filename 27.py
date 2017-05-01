import numpy as np
import random

while True:
    k = 0
    b = 12
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(0, 100)
    a = sum(arr)
    c = a / b
    x = min(arr)
    for i in arr:
        if i < 30:
            k += 1
    print(arr)
    print(k, a, c, x)
    break