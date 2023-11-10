# https://www.acmicpc.net/problem/9095

import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 12):
        dp[i] = sum(dp[i-3:i])
for _ in range(T):
    n = int(input())
    print(dp[n])

'''
n 일 때의 경우의 수
1) (n-1) 경우의 수에 각각 "+ 1" 추가 -> dp[n-1]
2) (n-2) 경우의 수에 각각 "+ 2" 추가 -> dp[n-2]
3) (n-3) 경우의 수에 각각 "+ 3" 추가 -> dp[n-3]
dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
'''