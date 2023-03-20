# in an even work, each letter occurs an event number of times.
# write a function solution that, given a string S consisting of N characters,
# returns the minimum number of letters that must be deleted to obtain an even word.

def solution(S):
    dict = {}
    for letter in S:
        dict[letter] = dict.get(letter, 0) + 1
    odd_count = 0
    for value in dict.values():
        if value % 2 != 0:
            odd_count += 1
    return odd_count

print(solution('acbcbba'))
print(solution('axxaxa'))
print(solution('aaaa'))