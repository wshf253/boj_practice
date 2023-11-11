# https://www.acmicpc.net/problem/9461

import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(T):
    N = int(input())
    print(dp[N])

# dp[i] = dp[i-3] + dp[i-2] also works, when i >= 4