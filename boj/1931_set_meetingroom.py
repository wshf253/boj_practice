import sys
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
    a, b = map(int, input().split())
    time = (a, b)
    meetings.append(time)
meetings.sort(key=lambda x : (x[1], x[0]))

cnt = 0
current = 0
for time in meetings:
    if time[0] >= current:
        cnt += 1
        current = time[1]
print(cnt)