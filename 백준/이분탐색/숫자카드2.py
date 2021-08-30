### 시간 초과 -> 다시풀기

n = int(input())

nList = list(map(int, input().split()))

m = int(input())

mList = list(map(int, input().split()))

def binarySearch(list, num):
    list.sort()
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == num:
            return mid
        elif list[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return False

for i in mList:
    search = binarySearch(nList, i)
    if not search:
        print('0')
    else:
        count = 0
        for j in nList:
            if i == j:
                count += 1
        print(count)