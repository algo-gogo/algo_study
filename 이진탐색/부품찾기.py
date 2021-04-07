# 정리: 입력받은 부품 N개가 있을 때 입력받은 M개의 종류의 부품이 있으면 yes, 없으면 No를 출력
# 입력: N 과 N개의 부품숫자, M 과 M개의 부품 숫자
# 출력 M개의 yes or NO

arrayN = []
arrayM = []
n = int(input())
arrayN = list(map(int, input().split()))
arrayN.sort()
m = int(input())
arrayM = list(map(int, input().split()))
arrayM.sort()


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, end - 1)


for i in arrayM:  # i 는 5 7 9
    result = binary_search(arrayN, i, 0, n - 1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")


##################################################
# 반복 이진 탐색

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

################################################################
# 계수 정렬
# array = [0] * 1000001
# arrayN = []
# arrayM = []
# n = int(input())
# arrayN = list(map(int, input().split()))       # 8 3 7 9 2
# arrayN.sort()
# m = int(input())
# arrayM = list(map(int, input().split()))       # 5 7 9
# arrayM.sort()
#
# for i in arrayN:
#     array[i] +=1
#
# for j in arrayM:
#     if array[j] != 0:
#         print("yes", end=" ")
#     else:
#         print("no", end=" ")
