import numpy as np
import random

while True:
    b = 15
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(10, 50)
    k = 1
    for i in arr:
        if i % 7 == 0:
            k *= i
    print (k)
    print(arr)
    break