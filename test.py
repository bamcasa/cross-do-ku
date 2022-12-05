import numpy as np
from pprint import pprint


def aa():
    global base
    base[0][0] = 1


base = np.array([[-1,  5,  0,  0, -1],
                 [0,  0,  0,  0,  5],
                 [0,  0, -1, -1,  0],
                 [6,  0,  0,  0,  0],
                 [0, -1, -1, -1,  0]], np.intc)
aa()
pprint(base)
