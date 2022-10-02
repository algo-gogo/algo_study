# 성냥개비 k개를 이용해서 숫자를 나타낸다.
# 숫자를 만드는데 0: 6개, 1: 2개, 2: 5개, 3: 5개, 4: 4개, 5: 5개, 6: 6개, 7: 3개, 8: 7개, 9: 6개 만큼 필요하다.
# 두 자리수 이상의 숫자를 만드는데 필요한 성냥개비 개수는 각 자릿수를 만드는데 필요한 성냥개비 개수의 합과 같다. 12 = 1(2) + 2(5) = 7개
# 1 <= k <= 50
# 성냥개비 k개를 모두 사용해서 만들 수 있는 숫자는 몇 가지 인가?

from itertools import permutations

def solution(k):
    if k == 1:
        return 0
    if k == 2:
        return 1
    num_list = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    count = 0
    for i in range(3):
        c = list(permutations(num_list, i))
        for j in c:
            if sum([num_list[k] for k in j]) == k:
                print(j)
                count += 1

    return count

print(solution(5))
# print(solution(6))
# print(solution(11))
# print(solution(1))
