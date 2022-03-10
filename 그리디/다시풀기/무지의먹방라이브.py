# https://programmers.co.kr/learn/courses/30/lessons/42891

def food_times_self(food_timesWithIndex, index):
    index2 = (index + 1) % len(food_timesWithIndex)
    if food_timesWithIndex[index][1] == 0:
        food_times_self(food_timesWithIndex, index2)
        return index2
    else:
        food_timesWithIndex[index2][1] = food_timesWithIndex[index2][1] - 1
        return index2


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    food_timesWithIndex = []
    for i in range(len(food_times)):
        value = food_times[i]
        food_timesWithIndex.append([i + 1, value])
    print(food_timesWithIndex)
    resultIndex = 0
    for i in range(k):
        index = i % len(food_times)
        if food_timesWithIndex[index][1] == 0:
            resultIndex = food_times_self(food_timesWithIndex, index)
        else:
            food_timesWithIndex[index][1] = food_timesWithIndex[index][1] - 1
            resultIndex = index

    resultIndex = food_times_self(food_timesWithIndex, resultIndex)
    print(food_timesWithIndex)
    print(resultIndex)
    return resultIndex + 1



# print(solution([3, 1, 2], 5))

# print(solution([5, 7, 5], 8))

# print(solution([4, 2, 7], 8))