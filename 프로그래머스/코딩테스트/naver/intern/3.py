from itertools import combinations

def collinear_check(point1, point2, point3):
    if point1.x == point2.x == point3.x or point1.y == point2.y == point3.y:
        return True
    try:
        if ((point3.y - point2.y) * (point2.x - point1.x) == (point2.y - point1.y) * (point3.x - point2.x)):
            return True
        if ((point2.y - point1.y / point2.x - point1.x) == (point3.y - point1.y / point3.x - point1.x) == (point3.y - point2.y / point3.x - point2.x)):
            return True
    except:
        return False
    return False

def solution(A):
    print(A)

    combi_list = list(combinations(A, 3))
    print(combi_list)

    num = 0
    for i in combi_list:
        correct = collinear_check(i[0], i[1], i[2])
        if correct:
            num += 1

    return num


print(solution([(0, 0), (1, 1), (2, 2), (3, 3), (3, 2), (4, 2), (5, 1)]))
