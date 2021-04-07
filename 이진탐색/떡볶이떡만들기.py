# 요약: 절단기의 높이를 지정하면 그만큼 절단한다.
# ex) 19, 14, 10, 17 이 있을 때  절단기 높이를 15 라고 하면 4, 0, 0, 2 => 6을 손님이 가져감

# 입력: 떡의 개수 n , 요청한 떡의 길이 m ex) 4, 6
# n 개의 떡의 길이                    ex) 19, 15, 10, 17
# 출력: 절단기를 설정 할 수 있는 최대 높이

n, m = map(int, input().split())

array = list(map(int, input().split()))

start = 0
end = max(array)

print(end)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in array:
        if i > mid:
            total = (total + i-mid)

    if total < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)