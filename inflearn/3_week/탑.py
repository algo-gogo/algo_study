### https://www.acmicpc.net/problem/2493

n = int(input())

num_list = list(map(int, input().split()))

# print(num_list)

# top_heights = [6, 9, 5, 7, 4]

def get_receiver_top_orders(heights):
    stack = []  # [인덱스, 높이]를 저장
    result = [0] * len(heights)

    for i in range(len(heights)):
        while stack and stack[-1][1] <= heights[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1][0] + 1
        stack.append([i, heights[i]])

    return result

get_receiver_top_orders(num_list)

# def get_receiver_top_orders(heights):
#     result = [0] * len(heights)
#     for i in range(len(heights) - 1, -1, -1):
#         for j in range(i - 1, -1, -1):
#             if heights[j] > heights[i]:
#                 result[i] = j + 1
#                 break
#     return result

# get_receiver_top_orders(num_list)

# def get_receiver_top_orders(heights):
#     result = []
#     for index, height in enumerate(heights):
#         stack = []
#         if index != 0:
#             for i in range(1, index + 1):
#                 stack.append(heights[i - 1])
#
#         if len(stack) == 0:
#             result.append(0)
#
#         while len(stack) > 0:
#             stack_index = len(stack)
#             pop_stack = stack.pop()
#             if height < pop_stack:
#                 result.append(stack_index)
#                 break
#             if len(stack) == 0:
#                 result.append(0)
#             stack_index -= 1
#
#     return result

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))