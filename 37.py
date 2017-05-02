import numpy as np
import random

while True:
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(-20, 20)
    m = len(arr) - 1
    while m > 0:
        for i in range(m):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        m -= 1
    print(arr)
    break