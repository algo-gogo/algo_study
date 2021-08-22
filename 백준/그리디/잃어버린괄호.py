arr = input().split("-")

print(arr)

### 55 / 50+40

result = 0
for i in arr[0].split("+"):
    result += int(i)

for i in arr[1:]:
    for j in i.split("+"):
        result -= int(j)

print(result)