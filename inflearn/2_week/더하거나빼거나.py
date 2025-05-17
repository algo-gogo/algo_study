numbers = [1, 1, 1, 1, 1]
target_number = 3
result = []
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    get_all_ways_by_doing_plus_or_minus(array, 0, 0)

    return result.count(target)

def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
    if current_index == len(array):  # 탈출조건!
        result.append(current_sum)  # 마지막 인덱스에 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
    get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])



print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!