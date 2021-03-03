# 내장 함수
# sum, min, max

result = sum([1, 2, 3, 4, 5])
result = min([1, 2, 3, 4, 5])
result = max([1, 2, 3, 4, 5])

# eval - 수학수식이 문자열 형식으로 들어오면 해당 수식을 계산해서 반환해줌
result = eval("(3+5) * 7")
print(result)

# sort는 원본을 바꿈
# sorted
result = sorted([7, 5, 3, 1, 9])
print(result)
result = sorted([7, 5, 3, 1, 9], reverse=True)

# 리스트의 원소로 리스트 or 튜플이 존재할 때 특정한 기준에 따라서 정렬 수행 정렬 기준은 key
result = sorted([('hong', 35), ('sun', 75), ('sdf', 34)], key=lambda x: x[1], reverse=True)
print(result)

