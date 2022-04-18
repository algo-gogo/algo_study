def division(number):
    division_list = []
    for n in range(1, number):
        if number % n == 0:
            division_list.append(n)
    return division_list


for i in range(1, 1000):
    if i == sum(division(i)):
        print(i)
