import numpy as np
import random

while True:
    c = int(input('vvvvv'))
    b = 20
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(1, 6)
    print(arr)
    f = 0
    for i in arr:
        if i != c:
            if i % 2 == 0:
                f += 1
        else:
            break
    print(f)
    break