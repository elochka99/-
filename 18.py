import numpy as np
while True:
    v = np.array(input('vedite').split(','), dtype = int)
    h = 0
    for i in v:
        if i < 0:
            h += i
    print(h)