# n 명의 학생 정보가 있을 때 각 학생의 이름과 성적 정보가 주어짐
# 성적이 낮은 순서대로 학생의 이름을 출력
# 입력: 학생수 , 학생수만큼의  이름과 성적
# 출력: 성적이 낮은 순의 학생 이름

n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# for arr in array:
#     array = sorted(array, key=arr[1])
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
