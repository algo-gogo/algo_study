# 큰 수부터 작은 순서로 정렬
# 입력 : 수열에 속해 있는 개수, 갯수만큼의 1 <= n <= 100,000 의 자연수
# 출력 :

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

print(array)