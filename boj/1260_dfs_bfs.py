import sys
input = sys.stdin.readline

vertex, edge, start = map(int, input().split())
graph = [[] for _ in range(vertex+1)]
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
for node in graph:
    node.sort()

# DFS
visited = [start]
def dfs(n):
    for node in graph[n]:
        if node not in visited:
            visited.append(node)
            dfs(node)
dfs(start)
print(*visited)

# BFS
visited = [start]
for node in visited:
    for adj in graph[node]:
        if adj not in visited:
            visited.append(adj)
print(*visited)

# using True, False
import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

def dfs(V):
    visited1[V] = True
    print(V, end=" ")
    for i in range(1, N+1):
        if not visited1[i] and graph[V][i]: # if i is not visited and i is connected with V
            dfs(i)

def bfs(V):
    q = deque([V])
    visited2[V] = True
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N+1):
            if not visited2[i] and graph[V][i]:
                q.append(i)
                visited2[i] = True

dfs(V)
print()
bfs(V)

# faster way
import sys
input = sys.stdin.readline
from collections import deque

vertex, edge, start = map(int, input().split())
graph = [[] for _ in range(vertex+1)]
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
for node in graph:
    node.sort()
visited1 = [False] * (vertex+1)
visited2 = [False] * (vertex+1)

def dfs(V):
    visited1[V] = True
    print(V, end=" ")
    for i in graph[V]:
        if not visited1[i]:
            dfs(i)

def bfs(V):
    q = deque([V])
    visited2[V] = True
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in graph[V]:
            if not visited2[i]:
                q.append(i)
                visited2[i] = True

dfs(start)
print()
bfs(start)