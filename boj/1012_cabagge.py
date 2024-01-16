import sys
input = sys.stdin.readline

# BFS
dx = [-1, 1, 0, 0]
dy  = [0, 0, -1, 1]

def BFS(x, y):
    queue = [(x, y)]
    mat[x][y] = 0

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if mat[nx][ny] == 1:
                queue.append((nx, ny))
                mat[nx][ny] = 0


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    mat = [[0]*(M) for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        mat[y][x] = 1

    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                BFS(i, j)
                cnt += 1
    print(cnt)


#DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy  = [0, 0, -1, 1]

def DFS(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            if mat[nx][ny] == 1:
                mat[nx][ny] -= 1
                DFS(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    mat = [[0]*(M) for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        mat[y][x] = 1

    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                DFS(i, j)
                cnt += 1
    print(cnt)