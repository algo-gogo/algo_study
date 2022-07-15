# 캐시
# def solution(cacheSize, cities):
#     if cacheSize == 0:
#         return 5 * len(cities)
#     answer = 0
#     cache = []
#     for i in cities:
#         city = i.upper()
#         if city in cache:
#             answer += 1
#             cache.remove(city)
#             cache.append(city)
#         else:
#             answer += 5
#             if len(cache) == cacheSize:
#                 del cache[0]
#             cache.append(city)
#
#     return answer


# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
#
# print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
# "NewYork", "Rome"]))

# print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))

### 효율성 4개중 2개 실패
# def solution(phone_book):
#     for index, value in enumerate(phone_book):
#         for index2, value2 in enumerate(phone_book):
#             if index == index2:
#                 pass
#             else:
#                 if value2.startswith(value):
#                     return False
#     return True

# def solution(phone_book):
#     for i in range(len(phone_book)):
#         for j in range(i + 1, len(phone_book)):
#             value1 = phone_book[i]
#             value2 = phone_book[j]
#             if value2.startswith(value1):
#                 return False
#             if value1.startswith(value2):
#                 return False
#     return True
#
# print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123", "456", "789"]))
# print(solution(["12", "123", "1235", "567", "88"]))

### 최소공배수
# import math
#
#
# def solution(arr):
#     answer = arr[0]
#     for i in arr:
#         answer = answer * i // math.gcd(answer, i)
#     return answer
#
#
# print(solution([2, 6, 8, 14]))
# # print(solution([1, 2, 3]))

### 오픈 채팅방
# def solution(record):
#     answer = []
#     answer_temp = {}
#     for i in record:
#         split = i.split(' ')
#         answer_temp[split[1]] = ('', [])
#
#     print(answer_temp)
#     for i in record:
#         split = i.split(' ')
#         if split[0] == 'Enter':
#             answer_temp[split[1]][0] = split[2]
#             answer_temp[split[1]][1].append('Enter')
#         if split[0] == 'Leave':
#             answer_temp[split[1]][0] = split[2]
#             answer_temp[split[1]][1].append('Leave')
#         if split[0] == 'Change':
#             answer_temp[split[1]][0] = split[2]
#
#     return answer

def solution(record):
    answer = []
    answer_temp = {}

    for i in record:
        split = i.split(' ')
        if split[0] == 'Enter':
            answer_temp[split[1]] = split[2]
            content = split[1] + " Enter"
            answer.append(content)
        if split[0] == 'Leave':
            content = split[1] + " Leave"
            answer.append(content)
        if split[0] == 'Change':
            answer_temp[split[1]] = split[2]

    result = []
    for i in answer:
        split = i.split(' ')
        real_name = answer_temp[split[0]]
        if split[1] == 'Enter':
            content = real_name + "님이 들어왔습니다."
            result.append(content)
        elif split[1] == 'Leave':
            content = real_name + "님이 나갔습니다."
            result.append(content)

    return result

print(solution(
    ["Enter uid1234 Muzi",
     "Enter uid4567 Prodo",
     "Leave uid1234",
     "Enter uid1234 Prodo",
     "Change uid4567 Ryan"]))
