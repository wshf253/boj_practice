# https://www.acmicpc.net/problem/1966
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, target = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    order = 0
    while True:
        max_prior = max(queue)
        front = queue.popleft()
        target -= 1
        if front >= max_prior:
            order += 1
            if target == -1:
                break
        else:
            queue.append(front)
            if target == -1:
                target = len(queue)-1
    print(order)