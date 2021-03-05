n = int(input())

# 500 100 50 10

count = 0

while n > 0:
    if n % 500 == 0:
        count += 1
        n -= 500
    elif n % 100 == 0:
        count += 1
        n -= 100
    elif n % 50 == 0:
        count += 1
        n -= 50
    elif n % 10 == 0:
        count += 1
        n -= 10

print(count)
# O(n)
#######################################################################

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

# O(coin_types)
