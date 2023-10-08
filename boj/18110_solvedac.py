# https://www.acmicpc.net/problem/18110

import sys
input = sys.stdin.readline

n = int(input())
boundary = int(n*0.15+0.5)
difficulty = []
for _ in range(n):
    difficulty.append(int(input()))
difficulty.sort()
difficulty = difficulty[boundary:n-boundary]
#print(difficulty)
if n == 0:
    print(0)
else:
    mean = sum(difficulty) / (n-2*boundary)
    print(int(mean+0.5))
# for rounding up, can add 0.5 and convert to int
# for example, int 5.9 -> 5 int 6.1 -> 6
# original num 5.4 -> int 5.4 + 0.5 -> 5
# original num 5.6 -> int 5.6 + 0.5 -> 6
# for negative number add -0.5, ex) -0.6 + -0.5 -> -1.1 -> -1

# python round function choose even num when there is 2 choices, round(2.5) -> 2