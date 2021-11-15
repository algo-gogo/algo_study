# 캐릭터의 점수 N
# N을 자릿수를 기준으로 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황
# 맞다면 LUCKY
# 아니면 READY
# 입력은 항상 짝수
# 입력: 123402
# 출력: LUCKY

n = input()

length = len(n)

first = 0
second = 0
for i in range(length // 2):
    first += int(n[i])

for j in range(length // 2, length):
    second += int(n[j])
# print(first)
# print(second)
if first == second:
    print("LUCKY")
else:
    print("READY")