# https://www.acmicpc.net/problem/18111

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
land = [0] * N
for i in range(N):
    land[i] = list(map(int, input().split()))
highest = max(land)
