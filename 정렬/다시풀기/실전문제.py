####################################### 위에서 아래로

# n = int(input())
# n_list = []
# for i in range(n):
#     a = int(input())
#     n_list.append(a)
#
# print(n_list)
#
# n_list.sort()
# for i in n_list:
#     print(i, end=' ')

####################################### 성적이 낮은 순서로 학생 출력하기


# n = int(input())
# n_dic = {}
#
# for i in range(n):
#     a, b = map(str, input().split())
#     n_dic[a] = b
#
# sorted_dict = sorted(n_dic.items(), key=lambda item: item[1], reverse=True)
# print(sorted_dict)
# for key, value in sorted_dict:
#     print(key, end=' ')

####################################### 두 배열의 원소 교체

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
print(a)
print(b)

for i in range(k):
    if a[i] > b[i]:
        break
    a[i], b[i] = b[i], a[i]

print(sum(a))

