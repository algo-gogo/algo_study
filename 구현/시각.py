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
