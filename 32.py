import numpy as np
import random

while True:
    b = 5
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(-10, 10)
    print(arr)
    for i in arr:
        if i < 0 and i % 2 == 0:
            print('ooooeeeeeee')


    break