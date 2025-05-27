# https://www.acmicpc.net/problem/2302
seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 1
}
def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    result = 1
    seat_array = [0] * total_count
    print(seat_array)
    for fixed in fixed_seat_array:
        seat_array[fixed - 1] = 1

    print(seat_array)
    count = 0
    for i in range(total_count):
        if seat_array[i] == 0:
            count += 1
        else:
            # fibo(count)
            result *= fibo_dynamic_programming(count + 1, memo)
            count = 0

    if count != 0:
        result *= fibo_dynamic_programming(count + 1, memo)
    return result


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))