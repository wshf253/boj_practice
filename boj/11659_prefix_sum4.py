import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sumList = [0]
for i in range(1, N+1):
    sumList.append(sumList[i-1] + nums[i-1])
    # sumList[2] -> sum from 1~2
#print(sumList)
for _ in range(M):
    i, j = map(int, input().split())
    result = sumList[j] - sumList[i-1]   
    # not sum[j] - sum[i] -> getting prefix sum of i+1~j 
    # ex) sum[3] - sum[1] -> sum of 2~3, sum[3] - sum[0] -> sum of 1~3
    print(result)