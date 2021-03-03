a = [1, 2, 3, 4, 5, 6, 7]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

# 다른 방법
# result = [i for i in a if i not in remove_set]

print(result)
