import numpy as np
import random

while True:
    b = 5
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(0, 5)
    g = 0
    for i in arr:
        if i != 0 and i % 2 == 0:
            g += i
        elif i == 0:
            break
    print(arr)
    print(g)

    break