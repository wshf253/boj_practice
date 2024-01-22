import sys
input = sys.stdin.readline

def bfs(n, k):
    visited = [False for _ in range(100001)]
    time = 0
    queue = [[n]]
    while queue:
        nodes = queue.pop(0)
        if k in nodes:
            return time
        tmp = []
        for node in nodes:
            if not visited[node]:
                visited[node] = True
                if node > 0 and not visited[node-1]:
                    tmp.append(node-1)
                if node < 100000 and not visited[node+1]:
                    tmp.append(node+1)
                if node < 50001 and not visited[2*node]:
                    tmp.append(2*node)
        queue.append(tmp)
        time += 1

n, k = map(int, input().split())
print(bfs(n, k))


# other way
from collections import deque
MAX = 100001

def bfs(n, k):
    distance = [0] * MAX
    q = deque([n])
    while q:
        v = q.popleft()
        if v == k:
            return distance[v]
        for next in [v-1, v+1, 2*v]:
            if 0 <= next < MAX and not distance[next]:
                distance[next] = distance[v] + 1
                q.append(next)

n, k = map(int, input().split())
print(bfs(n, k))