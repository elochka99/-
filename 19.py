import numpy as np
import random

while True:
    b = 20
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(200, 300)
    k = 0
    for i in arr:
        if i % 3 == 2:
            k += i
    print (arr)
    print(k)
    break