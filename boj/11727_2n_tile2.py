# https://www.acmicpc.net/problem/11727

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3
for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2] * 2
print(dp[n] % 10007)

# i 번째 방법의 수는 (i-1) 번째에서 1x2(가로x세로) 타일 추가와 (i-2)번째에서 2x1, 2x2 타일 2가지 추가하는 경우