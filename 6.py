import numpy as np
import random
while True:
    k = 0
    b = 8
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(-10, 10)
        if arr[j] < 0:
            k+=1
    print(arr)
    print(k)
    break