# 가장 긴 점포
# 특수문자 포함된 점포
#
def solution(merchantNames):
    answer = []
    a = {}
    store_name = ''
    for i in range(len(merchantNames)):
        if store_name == '':
            a[1] = [merchantNames[i]]
            store_name = merchantNames[i]

    print(a)
    return answer


print(solution([
    ["토스커피사일로 베이커리", "토스커피사일", "토스커피사일로 베이커", "토스커피사일로 베이", "토스커피사일로&베이커리"]]))
# ["토스커피사일로&베이커리"]

print(solution(
    ["비바리퍼블리", "토스커피사일로 베이커리", "비바리퍼블리카 식당", "토스커피사일", "토스커피사일로 베이커", "비바리퍼블리카식", "토스커피사일로 베이", "토스커피사일로&베이커리"]))
# ["토스커피사일로&베이커리", "비바리퍼블리카 식당"]
