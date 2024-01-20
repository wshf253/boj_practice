import sys
input = sys.stdin.readline

def sol(n, paper, ans):
    res = sum(sum(paper[i]) for i in range(n))
    if res == n*n:
        ans[1] += 1
    elif res == 0:
        ans[0] += 1
    else:
        jump = int(n/2)
        dx = [0, 0, jump, jump]
        dy = [0, jump, 0, jump]
        for a in range(4):
            new = [[0] * (jump) for _ in range(jump)]
            for i in range(jump):
                for j in range(jump):
                    new[i][j] = paper[i + dx[a]][j + dy[a]]
            sol(jump, new, ans)

ans = [0, 0]
N = int(input())
paper = [[0] * (N) for _ in range(N)]
for i in range(N):
    paper[i] = list(map(int, input().split()))

sol(N, paper, ans)
        
print(ans[0])
print(ans[1])


# other way
import sys
input = sys.stdin.readline

blue, white = 0, 0
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def divide(x, y, N):
    global blue, white
    cnt = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j]:
                cnt += 1
    if cnt == N*N:
        blue += 1
    elif cnt == 0:
        white += 1
    else:
        divide(x, y, N//2)
        divide(x + N//2, y, N//2)
        divide(x, y + N//2, N//2)
        divide(x + N//2, y + N//2, N//2)

divide(0, 0, N)
print(white)
print(blue)


# get the first color and compare the rest with it\
import sys
input = sys.stdin.readline

blue, white = 0, 0
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def divide(x, y, N):
    global blue, white
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] != color:
                divide(x, y, N//2)
                divide(x + N//2, y, N//2)
                divide(x, y + N//2, N//2)
                divide(x + N//2, y + N//2, N//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1    

divide(0, 0, N)
print(white)
print(blue)