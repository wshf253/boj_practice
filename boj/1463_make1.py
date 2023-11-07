# https://www.acmicpc.net/problem/1463

# using graph (BFS) -> bfs로 탐색한 결과는 최단거리 보장
from collections import deque

N = int(input())
BFS = deque([N])
visited = [0] * (N+1)
while BFS:
    n = BFS.popleft()
    if n == 1:
        break
    if n%3 == 0 and visited[n//3] == 0:
        # if visited[n//3] is not 0, it means that it already has minimum operations
        visited[n//3] = visited[n] + 1
        BFS.append(n//3)
    if n%2 == 0 and visited[n//2] == 0:
        visited[n//2] = visited[n] + 1
        BFS.append(n//2)
    if visited[n-1] == 0:
        visited[n-1] = visited[n] + 1
        BFS.append(n-1)
print(visited[1])


# dp - bottomup, from 1 -> N
N = int(input())
dp = [0] * (N+1) # dp[n] has min op for n to become 1
for i in range(2, N+1): # from 2~N since 1 needs 0 op to become 1, dp[1] will be 0
    dp[i] = dp[i-1] + 1
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[N])
'''
N = 3, dp[1] = 0
dp[2] = dp[1] + 1 = 1
2%2==0 -> dp[2] = dp[1] + 1 = 1
dp[2] = min(1,1) -> 1
dp[3] = dp[2] + 1 = 2
3%3==0 -> dp[3] = dp[3/3] + 1 = dp[1] + 1 = 1
dp[3] = min(2, 1) = 1
dp[3] = 1
'''

# dp - topdown, from N -> 1
N = int(input())
dp = {1:0}
def rec(n):
    if n in dp.keys():
        return dp[n]
    if (n%3==0) and (n%2==0):
        dp[n] = min(rec(n//3)+1, rec(n//2)+1)
    elif n%3==0:
        dp[n] = min(rec(n//3)+1, rec(n-1)+1)
    elif n%2==0:
        dp[n] = min(rec(n//2)+1, rec(n-1)+1)
    else:
        dp[n] = rec(n-1) + 1
    return dp[n]
print(rec(N))