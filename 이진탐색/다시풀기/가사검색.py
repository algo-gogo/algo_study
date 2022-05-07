# https://github.com/ndb796/python-for-coding-test/blob/master/15/4.py

# def solution(words, queries):
#     result_list = []
#
#     for i in queries:
#         result = 0
#         for j in words:
#             if len(i) == len(j):
#                 split_list = i.split('?')
#                 if split_list[0] == '' and split_list[-1] == '':
#                     result += 1
#                 elif split_list[0] != '':
#                     if j.startswith(split_list[0]):
#                         result += 1
#                 else:
#                     if j.endswith(split_list[-1]):
#                         result += 1
#         result_list.append(result)
#     return result_list

### 트라이 알고리즘??
import sys

sys.setrecursionlimit(100001)


def solution(words, queries):
    answer = []

    rev_words, counted = [], []  # 조건 b, c를 위한 두 변수
    for w in words:
        rev_words.append(w[::-1])
        counted.append(len(w))

    trie = make_trie({}, words)  # 조건 a 의 trie
    rev_trie = make_trie({}, rev_words)  # 조건 b 의 rev_trie

    for query in queries:  # 3가지 조건으로 나누어서,
        if query[0] == '?' and query[-1] == '?':
            answer.append(counted.count(len(query)))
        elif query[0] == '?':
            answer.append(search_trie(rev_trie, query[::-1], len(query)))
        elif query[-1] == '?':
            answer.append(search_trie(trie, query, len(query)))

    return answer


def make_trie(trie, words):
    for word in words:
        cur = trie
        l = len(word)
        for w in word:
            if w in cur:
                cur = cur[w]
                cur['!'].append(l)
            else:
                cur[w] = {}
                cur = cur[w]
                cur['!'] = [l]
    return trie


def search_trie(trie, query, length):
    count = 0
    if query[0] == '?':
        return trie['!'].count(length)
    elif query[0] in trie:
        count += search_trie(trie[query[0]], query[1:], length)

    return count


# from bisect import bisect_left, bisect_right
#
#
# # 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, right_value)
#     left_index = bisect_left(a, left_value)
#     return right_index - left_index
#
#
# # 모든 단어들을 길이마다 나누어서 저장하기 위한 리스트
# array = [[] for _ in range(10001)]
# # 모든 단어들을 길이마다 나누어서 뒤집어 저장하기 위한 리스트
# reversed_array = [[] for _ in range(10001)]
#
#
# def solution(words, queries):
#     answer = []
#     for word in words:  # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
#         array[len(word)].append(word)  # 단어를 삽입
#         reversed_array[len(word)].append(word[::-1])  # 단어를 뒤집어서 삽입
#
#     for i in range(10001):  # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
#         array[i].sort()
#         reversed_array[i].sort()
#
#     for q in queries:  # 쿼리를 하나씩 확인하며 처리
#         if q[0] != '?':  # 접미사에 와일드 카드가 붙은 경우
#             res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
#         else:  # 접두사에 와일드 카드가 붙은 경우
#             res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
#         # 검색된 단어의 개수를 저장
#         answer.append(res)
#     return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))
