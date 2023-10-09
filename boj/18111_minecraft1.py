# https://www.acmicpc.net/problem/18111
# get min and max height, set the goal height to numbers between min and max, update if time is min
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
res_time = -1
res_h = 0
for i in range(minH, maxH+1):
    time = 0
    cur_B = B
    for h in land.keys():
        if h > i:
            diff = h - i
            cur_B += land[h] * diff
            time += 2 * land[h] * diff
    for h in land.keys():
        if h < i:
            diff = i - h
            if cur_B < land[h] * diff:
                time = -1
                break
            else:
                cur_B -= land[h] * diff
                time += land[h] * diff
    if time == -1:
        continue
    elif res_time == -1:
        res_time = time
        res_h = i
    elif res_time >= time:
        res_time = time
        res_h = i
print(res_time, res_h)

'''
land = [0] * N
for i in range(N):
    land[i] = list(map(int, input().split()))
maxH = max(land)
minH = min(land)
res_time = -1
res_h = 0
for i in range(minH, maxH+1):
    time = 0
    for h in land:
    

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
res_time = -1
res_h = 0
for i in range(minH, maxH+1):
    time = 0
    cur_B = B
    for h in land.keys():
        if h > i:
            diff = h - i
            cur_B += land[h] * diff
            time += 2 * land[h] * diff
    for h in land.keys():
        if h < i:
            diff = i - h
            if cur_B < land[h]:
                time = -1
                break
            else:
                cur_B -= land[h] * diff
                time += land[h] * diff
    if time == -1:
        continue
    elif res_time == -1:
        res_time = time
        res_h = i
    elif res_time >= time:
        res_time = time
        res_h = i
print(res_time, res_h)
'''