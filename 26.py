import numpy as np
while True:
    v = np.array(input('vedite').split(','), dtype = int)
    b = max(v)
    n = min(v)
    c = sum(v) / len(v)
    print(b, n, c)