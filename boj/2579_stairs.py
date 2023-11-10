# https://www.acmicpc.net/problem/2579

# 참고: https://v3.leedo.me/devs/64
import sys
input = sys.stdin.readline

n = int(input())
stair = [0] * 301 # [0] * (n+1) -> cause error when n is smaller than 3
for i in range(n):
    stair[i+1] = int(input())
score = [0] * 301
score[1] = stair[1]
score[2] = stair[1] + stair[2]
score[3] = max(stair[1] + stair[3], stair[2] + stair[3])
for i in range(4, n+1):
    score[i] = max(stair[i] + stair[i-1] + score[i-3], stair[i] + score[i-2])

print(score[n])