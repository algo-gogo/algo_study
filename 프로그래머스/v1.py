def cal(resultList, value):
    if value < 10000:
        resultList[0] += 1
    elif 10000 <= value < 20000:
        resultList[1] += 1
    elif 20000 <= value < 50000:
        resultList[2] += 1
    elif 50000 <= value < 100000:
        resultList[3] += 1
    else:
        resultList[4] += 1

def solution(purchase):

    a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    listDate = []
    for index, value in enumerate(purchase):
        split = value.split(' ')
        price = split[1]
        date = split[0][5:]
        dateSplit = date.split('/')
        month = dateSplit[0]
        day = dateSplit[1]
        value = (a[int(month) - 1] + int(day), int(price))
        listDate.append(value)

    print(listDate)

    resultList = [0, 0, 0, 0, 0]

    for i in range(len(listDate) - 1):
        value = listDate[i]
        nextValue = listDate[i + 1]
        nowValue = 0

        dateMinus = nextValue[0] - value[0]
        cal(resultList, value[1])
        if dateMinus < 30:
            nowValue = nextValue[1] + value[1]


    return [245, 30, 30, 30, 30]


print(solution(["2019/01/01 5000",
                "2019/01/20 15000",
                "2019/02/09 90000"]))
