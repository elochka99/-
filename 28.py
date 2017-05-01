import numpy as np
import random

while True:
    b = 20
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(150, 300)
    f = 0
    for i in arr:
        if i % 2 == 0:
            f += 1
    print(arr)
    print(f)
    break