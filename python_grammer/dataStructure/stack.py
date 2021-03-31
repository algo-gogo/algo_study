# 선입후출, 후입선출
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(1)
stack.append(1)
stack.pop()



print(stack[-1])

print(stack)
print(stack[::-1])