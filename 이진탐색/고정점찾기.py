n = int(input())

nList = list(map(int, input().split()))

def binarySearch(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        if mid > array[mid]:
            start = mid + 1
        if mid < array[mid]:
            end = mid - 1
    return -1


search = binarySearch(nList, 0, n - 1)
print(search)
