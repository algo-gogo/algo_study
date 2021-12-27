n, x = map(int, input().split())

array = list(map(int, input().split()))

def binarySearch(array, start, end, target):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            result += 1
            i = 1
            while True:
                if array[mid + i] == target:
                    result += 1
                    i += 1
                else:
                    break
            i = 1
            while True:
                if array[mid - i] == target:
                    result += 1
                    i += 1
                else:
                    break
            return result
        if target > array[mid]:
            start = mid + 1
        if target < array[mid]:
            end = mid - 1
    result = -1
    return result

print(binarySearch(array, 0, n - 1, x))