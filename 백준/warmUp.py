### 문자열
# word = str(input().upper())
# print(word)
#
# removeSameWord = list(set(word))
# print(list(word))
# print(removeSameWord)
#
# woldCountList = []
# for i in removeSameWord:
#     count = word.count(i)
#     print(count, i)
#     woldCountList.append(count)
#
# if woldCountList.count(max(woldCountList)) > 1:
#     print('?')
# else:
#     maxIndex = woldCountList.index(max(woldCountList))
#     print(removeSameWord[maxIndex])


# word = str(input())
# print(list(word))
#
# print(list(set(word)))
# removeSameWord = list(word)
# removeSameWord = ' '.join(removeSameWord).split()
# print(removeSameWord)
#
# print(len(removeSameWord))

array = list(map(str, input().split()))
print(len(array))