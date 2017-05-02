# 41
import numpy as np
import random

while True:
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(0, 201)
    print(arr)
    s = sorted(arr)
    k = max(s)
    print(s, k)
    e = 0
    for i in s:
        if i == k:
            e += 1
    print(e)
    if e > 1:
        print('chislo govno')
        break
    else:
        y = int(input('vedite'))
        if k < y:
            print("True")
        else:
            print('xuba')