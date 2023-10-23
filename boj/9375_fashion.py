import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = {}
    days = 1
    for _ in range(n):
        name, type = input().split()
        if type in clothes.keys():
            clothes[type] += 1
        else:
            clothes[type] = 1
    for val in clothes.values():
        days *= (val + 1)
    days -= 1
    print(days)

# days *= (val + 1) -> (해당 종류의 옷 개수 + 해당 종류의 옷을 안 입는 경우 1)을 차례대로 곱해준다
# 마지막에 옷을 안 입고 있는 경우 제외를 위해 -1을 해준다.