# a = [1, 2, 3, 4]
#
# b = a[:]
# b[1] = 0
# print(a, b)
#
# a = [[0], [1], [2]]
# b = a[:]
# b[0][0] = 1
# print(a, b)

a = [[0], [1], [2]]
b = [item[:] for item in a]
b[0][0] = 1
print(a, b)