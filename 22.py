import numpy as np
import random

while True:
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(5, 500)
    k = 1
    for i in arr:
        if i % 3 == 0 and i % 9 == 0:
            k *= i
    print(arr)
    print(k)

    break