# https://www.acmicpc.net/problem/2606

import sys
input = sys.stdin.readline

n = int(input())
pair = int(input())
graph = {}
infected = [1]
for _ in range(pair):
    a, b = map(int, input().split())
    if a in graph.keys():
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph.keys():
        graph[b].append(a)
    else:
        graph[b] = [a]
for i in infected:
    if 1 not in graph.keys():
        break
    # 1이 연결되지 않은 경우, 답은 0
    for vertex in graph[i]:
        if vertex in infected:
            continue
        infected.append(vertex)
print(len(infected)-1)
# 1번 컴퓨터를 통해 감염되는 수 이므로 1번은 제외

# BFS
from collections import deque
n = int(input())
v = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1) # if infected 1, else 0
for _ in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
visited[1] = 1
que = deque([1])
while que:
    infect = que.popleft()
    for com in graph[infect]:
        if visited[com] == 0:
            que.append(com)
            visited[com] += 1
print(sum(visited)-1)

# DFS
n = int(input())
v = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1) # if infected 1, else 0
for _ in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
def dfs(v):
    visited[v] = 1
    for com in graph[v]:
        if visited[com] == 0:
            dfs(com)
dfs(1)
print(sum(visited)-1)