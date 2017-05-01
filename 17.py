import numpy as np
import random

while True:
    b = 20
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.uniform(100, 200)
    print(arr)
    c = arr[1::2]
    print(c)
    print(sum(c))

    break