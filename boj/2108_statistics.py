# https://www.acmicpc.net/problem/2108

# original version, using dictonary to find most frequent num
import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()
mean = sum(numbers) / N
print(round(mean))
median = numbers[int(N/2)]
print(median)
numDic = {}
for num in numbers:
    if num in numDic.keys():
        numDic[num] += 1
    else:
        numDic[num] = 1
freqList = [key for key, val in numDic.items() if max(numDic.values()) == val]
if len(freqList) > 1:
    print(freqList[1])
else: print(freqList[0])
range = numbers[-1] - numbers[0]
print(range)


# since the absolute value of num is 4000, 
# create 8001 size array, and count each num by adding 4000
import sys
input = sys.stdin.readline

N = int(input())
numbers = []
cnt = [0 for _ in range(8001)]
for _ in range(N):
    num = int(input())
    numbers.append(num)
    cnt[num+4000] += 1
numbers.sort()
mean = sum(numbers) / N
median = numbers[N//2]
check = 0
max = max(cnt)
for i in range(8001):
    if max == cnt[i]:
        freq = i-4000
        check += 1
    if check == 2:
        break
range = numbers[-1] - numbers[0]
print(round(mean))
print(median)
print(freq)
print(range)