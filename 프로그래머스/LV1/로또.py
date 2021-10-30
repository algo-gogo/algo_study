# def solution(lottos, win_nums):
#     removeNum = 0
#     for i in lottos:
#         if i == 0:
#             removeNum += 1
#     result = 0
#
#     for i in lottos:
#         for j in win_nums:
#             if i == j:
#                 result += 1
#
#     maxNum = 7 - removeNum - result
#     if maxNum > 5:
#         maxNum = 6
#     minNum = 7 - result
#     if minNum > 5:
#         minNum = 6
#
#     answer = []
#     answer.append(maxNum)
#     answer.append(minNum)
#     return answer

### 다른사람 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]