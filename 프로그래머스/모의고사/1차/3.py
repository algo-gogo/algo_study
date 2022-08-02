def solution(order):
    answer = 0
    stack = []

    # order 의 등록된 수
    now = 0
    # 트럭의 짐
    zim = 1
    result_list = []
    max_num = max(order)
    while True:
        try:
            if max_num + 1 < zim:
                break
            if zim == order[now]:
                result_list.append(order[now])
                zim += 1
                now += 1
            elif len(stack) > 0 and stack[-1] == order[now]:
                stack.pop()
                result_list.append(order[now])
                now += 1
            else:
                stack.append(zim)
                zim += 1
        except:
            zim += 1

    return len(result_list)


print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))
