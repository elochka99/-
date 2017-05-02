import numpy as np
import random

while True:
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(-10, 10)

    arr1 = np.zeros(b, dtype=int)
    for i in range(b):
        arr1[i] = random.randint(0, 30)
    print(arr, '\n', arr1)

    q = list()
    w = list()
    h = list()
    n = -1
    p = list()
    for i in arr:
        n += 1
        if i <= 0:
            p.append(n)
            h.append(i)
        elif i > 0:
            q.append(n)
            w.append(i)
    print(p)
    print(h)
    m = 0
    for i in p:
        m += arr1[i]
    print(m)

    z = 0
    for j in p:
        z += arr1[i]
    print(q, w, z)
    break

    """
    import numpy as np
import random

while True:
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(-10, 10)

    arr1 = np.zeros(b, dtype=int)
    for i in range(b):
        arr1[i] = random.randint(0, 30)
    print(arr, '\n', arr1)

    h = list()
    n = -1
    p = list()
    for i in arr:
        n += 1
        if i <= 0:
            p.append(n)
            h.append(i)
    print(p)
    print(h)
    m = 0
    for i in p:
        m += arr1[i]
    print(m)

    h = list()
    n = -1
    p = list()
    for i in arr:
        n += 1
        if i > 0:
            p.append(n)
            h.append(i)
    print(p)
    print(h)
    m = 0
    for i in p:
        m += arr1[i]
    print(m)

    break
    """