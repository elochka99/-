import numpy as np
import random

while True:
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(1, 5)

    arr1 = np.zeros(b, dtype=int)
    for i in range(b):
        arr1[i] = random.randint(0, 16)
    h = 0
    for i in arr:
        for j in arr1:
            if i == 2 and j > 8:
                h += 1
                break
    print(arr, '\n', arr1)

    print(h)
    break