# 외벽의 총 둘레는 n 미터
# 외벽의 취약 지점 점검
# 점검시간을 1시간 제한
# 최소한의 친구들을 투입해 취약 지점 점검
# 나머지는 내부 공사
# 정북 방향 0
# 취약지점은 정북으로부터 시계방향 떨어진 거리
# 친구들은 시계, 반시계 방향으로만 이동

# 외벽의 길이 n
# 취약 지점의 위치가 담긴 배열 weak
# 각 친구가 이동할 수 있는 거리 dist
# 취약 지점 점검 보낼 친구 수 의 최솟값

from itertools import combinations

def solution(n, weak, dist):

    nList = [0 for _ in range(n)]
    for i in weak:
        nList[i-1] = 1

    dist.sort(reverse=True)
    print(nList)
    print(dist)
    # 가장 짧은 곳부터 공략

    # weak 사이들의 거리 구하기
    weakList = []
    for i in range(len(weak)):
        j = i + 1
        if j >= len(weak):
            j = j % 4
        distance = abs(weak[i] - weak[j])
        ### 원형이기 때문에
        if distance > n // 2:
            distance = n - distance
        weakList.append((distance, i))

    weakList.sort(key=lambda x: x[0])
    print(weakList)


    answer = 0
    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
