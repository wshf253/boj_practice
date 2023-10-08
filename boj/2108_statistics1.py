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