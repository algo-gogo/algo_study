# 피트니스센터 가장 긴 예약 순서 찾기

# 15분 단위 예약 가능
# 최대 운동 예약시간은 90분을 못넘김
# 예약시간은 15분 단위로만 가능
# 한번 운동후 충전시간 필요
# 운동 예약 시간은 겹치지 않음
# 운동 예약 시간 스케줄 중에서 위의 조건에 맞추어 가장 길게 운동을 지도할 수 있는 예약 순서를 찾는 함수를 만들고 출력

def solution(schedules):
    answer = 0
    return answer

print(solution([30, 30, 60, 90, 60, 15, 15, 60])) # 210
print(solution([45, 15, 30])) # 75