import numpy as np
arr = np.array(input('vedite').split(','), dtype=int)
d = 0
for i in arr:
    if i > 0:
        d += i
print(d)