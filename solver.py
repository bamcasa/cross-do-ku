import numpy as np
from pprint import pprint


def merge(a: int, b: int):
    return [a, b]


def search_possible_cross(pos):
    y = pos[0]
    x = pos[1]

    n = base[y][x]  # 좌표 숫자크기
    # print(n)
    possible_cross = np.zeros(size)

    east = 1
    while x + east < size[0] and east <= n and base[y][x + east] == 0:
        possible_cross[y][x+east] += 1
        east += 1

    west = 1
    while base[y][x - west] == 0 and west <= n and x - west >= 0:
        possible_cross[y][x-west] += 1
        west += 1

    north = 1
    while base[y-north][x] == 0 and north <= n and y-north >= 0:
        possible_cross[y - north][x] += 1
        north += 1

    south = 1
    while y + south < size[0] and south <= n and base[y+south][x] == 0:
        possible_cross[y+south][x] += 1
        south += 1

    # print(possible_cross)

    return possible_cross


size = (5, 5)
base = np.zeros(size, np.intc)

base[0][1] = 5
base[1][4] = 5
base[3][0] = 6

base[0][4] = -1

base[2][2] = -1
base[2][3] = -1

base[4][1] = -1
base[4][2] = -1
base[4][3] = -1

# wall = -1

pprint(base)
print("\n")

pos_y, pos_x = np.where(base >= 1)
pos_list = list(map(merge, pos_y, pos_x))  # 합치기

possible_crosses = []

for pos in pos_list:
    possible_crosses.append(search_possible_cross(pos))
possible_crosses = np.array(possible_crosses)

pprint(possible_crosses)
# result = search_possible_cross(0, 1)

# result = search_possible_cross(3, 0)
