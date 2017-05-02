import numpy as np
import random

while True:
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(-20, 20)
    k = 0
    for i in arr:
        if -2 <= i <= 10:
            k += i
    print(arr, k)

    break