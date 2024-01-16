import sys
input = sys.stdin.readline

# 시간 초과
N = int(input())
heap = {}
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
            continue
        out = min(heap.keys())
        print(out)
        heap[out] -= 1
        if heap[out] == 0:
            heap.pop(out)
    else:
        if x in heap.keys():
            heap[x] += 1
        else:
            heap[x] = 1


from heapq import *
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, x)