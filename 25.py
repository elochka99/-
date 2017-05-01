import numpy as np
import random

while True:
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(10, 100)
    k = 1
    for i in arr:
        if i % 5 == 0:
            k *= i
    print(arr)
    print(k)

    break