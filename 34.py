import numpy as np
import random

while True:
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(10, 100)

    arr1 = np.zeros(b, dtype=int)
    for i in range(b):
        arr1[i] = random.randint(10, 100)

    b = arr * arr1
    print(arr, '\n', arr1, '\n', b)

    break