# https://www.acmicpc.net/problem/19236

graph = []
graph2 = []

for i in range(4):
    l = list(map(int, input().split()))
    a = []
    for j in range(4):
        i_ = l[j * 2:j * 2 + 2]
        i_.append(i)
        i_.append(j)
        ti = tuple(i_)
        a.append(ti)
        graph2.append(i_)
    graph.append(a)

moveList = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
print(graph)
print(graph2)
count = 0
count += graph2[0][0]
graph2[0][0] = 100

graph2.sort()
print(graph2)


def validateTurn45(x, y, direction):
    nx = x + moveList[direction % 8][0]
    ny = y + moveList[direction % 8][1]
    if nx == 0 and ny == 0:
        return validateTurn45(x, y, direction + 1)
    elif 0 <= nx < 4 and 0 <= ny < 4:
        return nx, ny
    else:
        return validateTurn45(x, y, direction + 1)


for value, direction, x, y in graph2:
    # 45도 회전해야하는지 체크
    if value == 100:
        continue
    nx, ny = validateTurn45(x, y, direction - 1)

    index1 = 0
    index2 = 0
    for index, i in enumerate(graph2):
        if i[2] == x and i[3] == y:
            index1 = index
        if i[2] == nx and i[3] == ny:
            index2 = index

    graph2[index1][2], graph2[index2][2] = graph2[index2][2], graph2[index1][2]
    graph2[index1][3], graph2[index2][3] = graph2[index2][3], graph2[index1][3]

print(graph2)
sharkPosition = graph2[-1]
sharkDirection = int(sharkPosition[1])
sharkX = sharkPosition[2]
sharkY = sharkPosition[3]


def findFish(sharkX_, sharkY_):
    global count
    for index_, g in enumerate(graph2):
        sharkNx = sharkX_ + moveList[sharkDirection - 1][0]
        sharkNy = sharkY_ + moveList[sharkDirection - 1][1]
        if g[2] == sharkNx and g[3] == sharkNy:
            count += graph2[index_][0]
            sharkX_ = sharkNx
            sharkY_ = sharkNy
            return findFish(sharkX_, sharkY_)
        elif 0 <= sharkNx < 4 and 0 <= sharkNy < 4:
            pass
        else:
            break
    return count


print(findFish(sharkX, sharkY))
print(count)

# for index, i in enumerate(graph2):
#     nx = sharkX + moveList[sharkDirection - 1][0]
#     ny = sharkY + moveList[sharkDirection - 1][1]
#     if i[2] == nx and i[3] == ny:
#         count += graph2[index][0]
