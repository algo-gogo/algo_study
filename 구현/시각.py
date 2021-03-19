# 요약 입력 받은 시간 n
# 0시0분0초 부터 n시 59분 59초 까지 모든 시각중에서 3이 하나라도 들어가는 경우의 수

n = int(input())

# n 59 59
count = 0

for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) or '3' in str(minute) or '3' in str(second):
                print( str(hour) + '시' + str(minute) + '분' + str(second))
                count += 1

print(count)

###############################################################

# n = int(input())
#
# # n 59 59
# count = 0
#
# for hour in range(n + 1):
#     for minute in range(60):
#         for second in range(60):
#             if hour % 10 == 3 or minute % 10 == 3 or second % 10 == 3:   # 0시 0분 31, 32 이런게 해당안됨
#                 count += 1
#
# print(count)
