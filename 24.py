import numpy as np
import random

while True:
    b = 30
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(500, 1000)
    k = 0
    for i in arr:
        if i % 5 == 0 and i % 8 == 0:
            k += i
    print(arr)
    print(k)

    break