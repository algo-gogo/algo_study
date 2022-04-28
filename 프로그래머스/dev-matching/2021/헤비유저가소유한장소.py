# https://programmers.co.kr/learn/courses/30/lessons/77487

# select *
# from PLACES
# where HOST_ID IN (
#     SELECT HOST_ID
#     from PLACES
#     group by HOST_ID
#     having count(ID) > 1
# )
