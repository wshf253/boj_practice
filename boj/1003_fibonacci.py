import sys
input = sys.stdin.readline

def fibonacci(n):
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    elif memo[0][n] != 0 and memo[1][n] != 0:
        return memo[0][n], memo[1][n]
    else:
        a0, a1 = fibonacci(n-1)
        b0, b1 = fibonacci(n-2)
        memo[0][n] = a0 + b0
        memo[1][n] = a1 + b1
        return memo[0][n], memo[1][n]

T = int(input())
for _ in range(T):
    N = int(input())
    memo = [[0 for _ in range(N+1)]] * 2
    ans = fibonacci(N)
    print(*ans)
# when using 2d array the value of memo[0][n] was same as memo[1][n]
# memo = [[0 for _ in range(N+1)]] * 2 -> memo[0][n] and memo[1][n] change together


# correct way
import sys
input = sys.stdin.readline

def fibonacci(n):
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    elif zero[n] != 0 and one[n] != 0:
        return zero[n], one[n]
    else:
        a0, a1 = fibonacci(n-1)
        b0, b1 = fibonacci(n-2)
        zero[n] = a0 + b0
        one[n] = a1 + b1
        return zero[n], one[n]

T = int(input())
for _ in range(T):
    N = int(input())
    zero = [0 for _ in range(N+1)]
    one = [0 for _ in range(N+1)]
    ans = fibonacci(N)
    print(*ans)

# using for loop
def fib(n):
    zeros = [1, 0, 1]
    ones = [0, 1, 1]
    if N >= 3:
        for i in range(2, N):
            zeros.append(zeros[i-1] + zeros[i])
            ones.append(ones[i-1] + ones[i])
    print(zeros[N], ones[N])

T = int(input())
for _ in range(T):
    N = int(input())
    fib(N)

# 규칙성 활용
# 0 출력 횟수와 1 출력 횟수를 N에 따라 정리하면
# N:0 -> 1/0, N:1 -> 0/1, N:2 -> 1/1, N:3 -> 1/2, N:4 -> 2/3, N:5 -> 3/5, N:6 -> 5/8
# 0의 출력 횟수는 (N-1)번째 1의 출력 횟수, 1의 출력 횟수는 (N-1)번째 0,1 출력 횟수의 합
# 또는 0: 1, (0, 1, 2, 3, 5...)  1: (0, 1, 2, 3, 5...) 규칙성이 같음
T = int(input())
for _ in range(T):
    N = int(input())
    zero, one = 1, 0
    for _ in range(N):
        zero, one = one, zero+one
    print(zero, one)