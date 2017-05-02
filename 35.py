import numpy as np
import random

while True:
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(-20, 10)
    m = len(arr) - 1
    c = 0
    while m > 0:
        for i in range(m):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                c += 1
        m -= 1
    if c > 0:
        print('masiv jopa', c, 'perestanovok')
        break
    else:
        print('masiv good')
        break