import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
times.sort()
time = 0
for i in range(N):
    time += sum(times[:i+1])
print(time)