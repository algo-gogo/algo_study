birth = ["1899-13-31", "19001231", "2001-09-04", "1900-02-29", "2021-5-31", "1950-11-30", "1996-02-29", "1999-11-31", "2000-02-29"]
# birth = ["-2019-12-29-", "1945--10-31", "----------", "20000-123-567"]
answer = 0

def check(birthday):
    if len(birthday) != 10:
        return False
    if birthday.count('-') != 2:
        return False
    months_with_31 = [1, 3, 5, 7, 8, 10, 12]
    months_with_30 = [4, 6, 9, 11]
    try:
        year, month, day = int(birthday.split("-")[0]), int(birthday.split("-")[1]), int(birthday.split("-")[2])
        if not 1900 <= year <= 2021:
            return False
        if not 1 <= month <= 12:
            return False
        yoonnyeon_flag = False
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
            yoonnyeon_flag = True
        if month == 2:
            if yoonnyeon_flag:
                if not 1 <= day <= 29:
                    return False
            else:
                if not 1 <= day <= 28:
                    return False
        if month in months_with_30:
            if not 1 <= day <= 30:
                return False
        if month in months_with_31:
            if not 1 <= day <= 31:
                return False
        return True

    except:
        return False



for day in birth:
    if not check(day):
        continue
    else:
        print(day)
        answer += 1

print(answer)