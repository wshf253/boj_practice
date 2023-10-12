import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memo = {}
for _ in range(N):
    site, pw = input().rstrip().split()
    memo[site] = pw
for _ in range(M):
    site = input().rstrip() # if no rstrip, site will be like "starlink.io\n" -> cause error
    print(memo[site])