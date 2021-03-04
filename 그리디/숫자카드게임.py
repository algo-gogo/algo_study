n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(list(map(int, input().split())))

drawing = []

for i in range(n):
    drawing.append(min(array[i]))

print(max(drawing))

#################################################################

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

##########################################################