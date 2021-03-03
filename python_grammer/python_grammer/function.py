a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()
print(a)

# global - 전역객체 가져다 쓸 때
# 람다 문법을 사용해서 아무거나 만들어보기
