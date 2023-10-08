# https://www.acmicpc.net/problem/15829
L = int(input())
string = input()
code = 97
map = {}
for i in range(26):
    map[chr(code+i)] = i+1
r = 31
M = 1234567891
sum = 0
for i in range(L):
    sum += map[string[i]] * r ** i
print(sum % M)

""""
for c, you have to do the mod for each loop to prevent overflow

1. (a + b) mod n = {(a mod n) + (b mod n)} mod n
2. (a - b) mod n = {(a mod n) - (b mod n)} mod n
3. (a * b) mod n = {(a mod n) * (b mod n)} mod n

H = ( a(0)*r(0) + a(1)*r(1) + ... + a(l-1)*r(l-1) ) % M
by rule1, H = sum( a(i)*r(i) % M) % M
by rule3, a(i)*r(i) % M = ( a(i) % M ) * ( r(i) % M ) % M
a(1) is much smaller than M
a(i)*r(i) % M = (a(i) * r(i) % M) % M
So, H = sum( a(i)*r(i) % M) % M = sum[{a(i) * (r(i) % M)} % M] % M
sum = 0
r = 1
for i in range(L):
    sum = (sum + map[string[i]] * r) % M
    r = (r*31) % M
print(sum)
"""