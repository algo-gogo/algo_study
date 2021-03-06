# https://programmers.co.kr/learn/courses/30/lessons/42891

def food_times_self(food_timesWithIndex, index, plusIndex):
    index2 = (index + 1) % len(food_timesWithIndex)
    if food_timesWithIndex[index2][1] == 0:
        food_times_self(food_timesWithIndex, index2, plusIndex)
        plusIndex += 1
        return index2, plusIndex
    else:
        food_timesWithIndex[index2][1] = food_timesWithIndex[index2][1] - 1
        return index2, plusIndex


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    food_timesWithIndex = []
    for i in range(len(food_times)):
        value = food_times[i]
        food_timesWithIndex.append([i + 1, value])
    print(food_timesWithIndex)
    resultIndex = 0
    plusIndex = 0
    for i in range(k):
        index = (i + plusIndex) % len(food_times)
        if food_timesWithIndex[index][1] == 0:
            print("i= ", i, end=' ')
            print(food_timesWithIndex)
            plusIndex += 1
            resultIndex, plusIndex = food_times_self(food_timesWithIndex, index, plusIndex)
        else:
            print("i= ", i, end=' ')
            print(food_timesWithIndex)
            food_timesWithIndex[index][1] = food_timesWithIndex[index][1] - 1
            resultIndex = index

    print("resultIndex", resultIndex)
    resultIndex, plusIndex = food_times_self(food_timesWithIndex, resultIndex, plusIndex)
    print(food_timesWithIndex)
    print(resultIndex)
    return resultIndex + 1



# print("답", solution([3, 1, 2], 5))
#
# print("답", solution([5, 7, 5], 8))

print("답", solution([4, 2, 7], 10))

######### 다른 답지

# def solution(food_times, k):
#     remain_list = []
#     length = len(food_times)
#
#     for i in range(length):
#         remain_list.append(i + 1)
#
#     current_round = 1
#
#     current_item = 0
#
#     t = 0
#     while t < k:
#         for i in remain_list[:]:
#             current_item = i
#             if food_times[i - 1] >= current_round:
#                 t += 1
#
#             if food_times[i - 1] <= current_round:
#                 remain_list.remove(i)
#
#             if t == k + 1:
#                 return i
#
#         current_round += 1
#
#         # print( remain_list )
#
#     if len(remain_list) > 0:
#         return current_item
#     else:
#         return -1
## remain_list[:]