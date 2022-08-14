# select name
# from phones
#          left outer join (
#     select (ifnull(cr.duration, 0) + ifnull(ce.duration, 0)) as duration, cr.phone_number
#     from (
#              select sum(duration) as duration, caller as phone_number
#              from calls
#              group by caller
#          ) cr
#              left outer join (
#         select sum(duration) as duration, callee as phone_number
#         from calls
#         group by callee
#     ) ce on cr.phone_number = ce.phone_number
# ) c on phones.phone_number = c.phone_number
# where c.duration >= 10
# order by phones.name
