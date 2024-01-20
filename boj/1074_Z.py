import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
order = 0

def divide(x, y, n):
    global order, r, c
    start = [order, order+(n//2)*(n//2), order+2*(n//2)*(n//2), order+3*(n//2)*(n//2)]
    if n == 2:
        for i in range(x, x+2):
            for j in range(y, y+2):
                if i == r and j == c:
                    print(order)
                order += 1
    else:
        if r < x+n//2 and c < y+n//2:
            order = start[0]
            divide(x, y, n//2)
        elif r < x+n//2 and c >= y+n//2:
            order = start[1]
            divide(x, y+n//2, n//2)
        elif r >= x+n//2 and c < y+n//2:
            order = start[2]
            divide(x+n//2, y, n//2)
        else:
            order = start[3]
            divide(x+n//2, y+n//2, n//2)

divide(0, 0, 2**N)


# other way
N, r, c = map(int, input().split())

def sol(N, r, c):
    if N == 0:
        return 0
    else:
        return 2*(r%2) + (c%2) + 4*sol(N-1, r//2, c//2)
print(sol(N, r, c))