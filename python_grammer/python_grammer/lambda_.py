# 람다식 연습
from functools import reduce

x = int(input())

plus_ten = lambda x: x + 10

print(plus_ten(x))

####################################

array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

result = list(filter(lambda x: x > 5 and x < 15, array))
print(result)


