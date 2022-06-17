from itertools import permutations

def split_data(plans):
    plan_list = []
    extra_list = []
    for index, value in enumerate(plans):
        temp = []
        split = value.split(' ')
        temp.append(int(split[0]))
        extra_service = split[1:]
        extra_list.extend(extra_service)
        temp.extend(extra_list)
        plan_list.append(temp)
    return plan_list


def solution(n, plans, clients):

    result_list = [0 for _ in range(len(clients))]
    print(result_list)

    for index, value in enumerate(clients):
        split = value.split(' ')
        data = int(split[0])
        extra_service = split[1:]

        plan_list = split_data(plans)
        for index2, value2 in enumerate(plan_list):
            data2 = value2[0]
            extra_service2 = value2[1:]
            if data <= data2:
                a = set(extra_service)
                b = set(extra_service2)
                c = a & b
                if a == a & b:
                    result_list[index] = index2 + 1
                    break

    return result_list

# print(solution(5, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"]))
print(solution(4, ["38 2 3", "394 1 4"], ["10 2 3", "300 1 2 3 4", "500 1"]))