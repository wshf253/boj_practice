import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
land = {}
for i in range(N):
    heights = list(map(int, input().split()))
    for height in heights:
        if height in land.keys():
            land[height] += 1
        else:
            land[height] = 1
maxH = max(land)
minH = min(land)
sol = [10**100, -1]
for i in range(minH, maxH+1):
    time = 0
    cur_B = B
    for h in land.keys():
        if h > i:
            diff = h - i
            cur_B += land[h] * diff
            time += 2 * land[h] * diff
        if h < i:
            diff = i - h
            cur_B -= land[h] * diff
            time += land[h] * diff
    if cur_B >= 0 and sol[0] >= time:
        sol = [time, i]
print(*sol)