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

    # 가능한 가지수, 동서남북 개수
    return possible_cross, [east-1, west-1, south-1, north-1]


def ovelap_crosses(crosses):
    cross = crosses[0]
    for i in range(1, len(crosses)):
        cross += crosses[i]
    return cross


def extend_cross(pos_i, n, direction):  # 동1 서2 남3 북4
    # 블럭의 번쨰수에서 뻗어나감
    global base
    # print(pos)
    pos = pos_list[pos_i]
    base[pos[0]][pos[1]] -= n
    if base[pos[0]][pos[1]] == 0:
        base[pos[0]][pos[1]] -= 1

    if direction == 0:  # 동
        i = 0
        j = 1
    elif direction == 1:
        i = 0
        j = -1
    elif direction == 2:
        i = 1
        j = 0
    elif direction == 3:
        i = -1
        j = 0

    for k in range(1, n+1):
        # print([pos[0] + k*i, pos[1] + k * j])
        base[pos[0] + k*i][pos[1] + k * j] -= 1
        correct_crosses[pos_i][pos[0] + k*i][pos[1] + k * j] += 1

    # print("ang!")


def check_perfect_cross(cross_news):
    i = 0
    for news in cross_news:
        sum1 = sum(news)
        if base[pos_y[i]][pos_x[i]] == sum1:  # 갈 수 있는 것과 뻗을 수 있는 것이 같은 경우
            extend_cross(i, news[0], 0)
            extend_cross(i, news[1], 1)
            extend_cross(i, news[2], 2)
            extend_cross(i, news[3], 3)
        i += 1
    print(base)


size = (5, 5)
base = np.zeros(size, np.intc)

base = np.array([[-1, -1, -1, -1, -1],
                 [0, -1, -1, -1, -1],
                 [5,  0,  0, -1, -1],
                 [0,  0,  1,  0, -1],
                 [0,  0,  0,  4,  0]], np.intc)

# wall = -1

pprint(base)
print("\n")

pos_y, pos_x = np.where(base >= 1)
pos_list = list(map(merge, pos_y, pos_x))  # 합치기

correct_crosses = np.zeros((len(pos_list), size[0], size[1]), np.intc)

# pprint(correct_crosses)


possible_crosses = []
possible_crosses_news = []

for pos in pos_list:
    temp = search_possible_cross(pos)
    possible_crosses.append(temp[0])
    possible_crosses_news.append(temp[1])

possible_crosses = np.array(possible_crosses)

check_perfect_cross(possible_crosses_news)  # check


possible_crosses = []
possible_crosses_news = []

for pos in pos_list:
    temp = search_possible_cross(pos)
    possible_crosses.append(temp[0])
    possible_crosses_news.append(temp[1])

possible_crosses = np.array(possible_crosses)
pprint(possible_crosses)
# print(possible_crosses_news)
# print(pos_y, pos_x)

check_perfect_cross(possible_crosses_news)  # check


possible_crosses = []
possible_crosses_news = []

for pos in pos_list:
    temp = search_possible_cross(pos)
    possible_crosses.append(temp[0])
    possible_crosses_news.append(temp[1])

possible_crosses = np.array(possible_crosses)

check_perfect_cross(possible_crosses_news)  # check


# overlap
# pprint(base)

pprint(correct_crosses)
