from collections import Counter

def solution(want, number, discount):
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    print(want_dict)

    result_list = []
    limit_length = len(discount) - 10
    for i in range(len(discount)):
        discount_slice = discount[i: i + 10]
        discount_counter = Counter(discount_slice)
        print(discount_counter)
        count = 0
        for w in want_dict:
            if discount_counter[w] >= want_dict[w]:
                count += 1
            else:
                result_list.append(False)
                break
            if len(want_dict) == count:
                result_list.append(True)

    print(result_list)

    return result_list.count(True)


print(solution(
    ['banana', 'apple', 'rice', 'pork', 'pot'], [3, 2, 2, 2, 1],
    ['chicken', 'apple', 'apple', 'banana', 'rice', 'apple', 'pork', 'banana', 'pork', 'rice', 'pot', 'banana', 'apple',
     'banana']))

# print(solution(
#     ['apple'], [10],
#     ['banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana']))
