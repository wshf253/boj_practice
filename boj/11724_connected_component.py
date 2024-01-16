'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u] += [v]
    graph[v] += [u]

connected = []
count = 0
for i in range(1, N+1):
    if graph[i] == [0]:
        continue
    connected = [i]
    count += 1
    for node in connected:
        for adj in graph[node]:
            if adj not in connected:
                connected.append(adj)
        graph[node] = [0]
    
print(count)


# DFS, faster way using visited array
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

cnt = 0
visited = [False] * (N+1)
for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)


'''

# BFS
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start, visited):
    queue = [start]
    visited[start] = True
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

cnt = 0
visited = [False] * (N+1)
for i in range(1, N+1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1

print(cnt)