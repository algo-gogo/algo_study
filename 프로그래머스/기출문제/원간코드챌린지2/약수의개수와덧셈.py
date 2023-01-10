def div_num(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        # 약수의 개수
        count = div_num(i)
        if count % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer

print(solution(13, 17))
print(solution(24, 27))