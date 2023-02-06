# merchants 테이블
# id(아이디), name(상호명), business_id(사업자 등록번호), tax_type(과세유형), category_id(업종 분류 아이디)
#
# card_usages 테이블
# id, created_at(사용일), category(구분 0이면 결제, 1이면 취소), amount(금액), merchant_id(결재 가맹점)
#
# 가장 돈을 많이 쓴 다섯 가맹점의 아이디, 이름, 사용한 금액 구하시오.

# SELECT
#   m.id as ID,
#   m.name as NAME,
#   sum(amount) AS '결제 금액'
# FROM merchants m
# JOIN card_usages c ON m.id = c.merchant_id
# where category = 0
# GROUP BY m.id
# ORDER BY sum(amount) DESC
# LIMIT 5;