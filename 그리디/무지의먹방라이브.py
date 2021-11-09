def solution(food_times, k):
    i = 0
    answer = 0
    eatFood = 0
    while k > 0:
        if i + 1 > len(food_times):
            i = i % 3
        if food_times[i] == 0:
            eatFood += 1
            if eatFood == len(food_times):
                answer = -1
                return answer
        else:
            food_times[i] -= 1
            k -= 1
        i += 1
    answer = i % 3 + 1
    return answer

# solution([3,1,2], 5)
# solution([5, 3, 5], 10)
# print(solution([3,1,2], 5))
print(solution([5, 3, 5], 10))