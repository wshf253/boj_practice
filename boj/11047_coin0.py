import sys
input = sys.stdin.readline

N, K = map(int, input().split())
types = []
for _ in range(N):
    types.append(int(input()))
# first element is always 1
min_coin = K
coinNum = 0
for i in range(1, N):
    if types[i] > K:
        break
    coinNum += K // types[i]
    left = K % types[i]
    for j in range(i, -1, -1):
        if types[j] > left:
            continue
        coinNum += left // types[j]
        left %= types[j]
    if coinNum < min_coin:
        min_coin = coinNum
    coinNum = 0
print(min_coin)


# simpler version

N, K = map(int, input().split())
types = []
for _ in range(N):
    types.append(int(input()))
count = 0
# each element is multiplier of previous one
for coin in reversed(types):
    count += K // coin
    K %= coin
print(count)