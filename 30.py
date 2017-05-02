import numpy as np
import random

while True:
    b = 20
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(1, 100)
    a = arr
    v = sorted(a)
    c = v[0]
    print(arr, '\n', v, '\n', c)
    k = 0
    for i in a:
        k +=1
        if i == c:
            print(k)
            break
    x = a[k:k+3]
    print(x)
    d = sum(x) / 3
    print(d)
    break