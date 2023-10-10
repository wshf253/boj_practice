# https://www.acmicpc.net/problem/11723

# first try, index 0~19 -> 1 if element exists, 0 if not
import sys
input = sys.stdin.readline

M = int(input())
set = [0 for _ in range(20)]
for _ in range(M):
    commands = input().split()
    if commands[0] == "add":
        num = int(commands[1])-1
        if set[num] == 0:
            set[num] = 1
    elif commands[0] == "remove":
        num = int(commands[1])-1
        if set[num] == 1:
            set[num] = 0
    elif commands[0] == "check":
        num = int(commands[1])-1
        if set[num] == 1:
            print("1")
        else:
            print("0")
    elif commands[0] == "toggle":
        num = int(commands[1])-1
        if set[num] == 1:
            set[num] = 0
        else:
            set[num] = 1
    elif commands[0] == "all":
        #set = [1 for _ in range(20)]
        set = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    else:
        #set = [0 for _ in range(20)] 
        set = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


# using python set
import sys
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    commands = input().split()
    if commands[0] == "add":
        num = int(commands[1])
        S.add(num)
    elif commands[0] == "remove":
        num = int(commands[1])
        S.discard(num) # reomve give error when there is no "num" in set, but discard doesn't
    elif commands[0] == "check":
        num = int(commands[1])
        if num in S:
            print("1")
        else: 
            print("0")
    elif commands[0] == "toggle":
        num = int(commands[1])
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif commands[0] == "all":
        #S = set(range(1,21))
        S = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    else:
        S = set()


# use bitmasking, 1 means the element exists, 0 means not exists, << means left shift
# 1<<0 = 1 (1), 1<<1 = 10 (2), 1<<2 = 100 (4), 1<<3 = 1000(8) so input-1
import sys
input = sys.stdin.readline

M = int(input())
S = 0
for _ in range(M):
    commands = input().split()
    if len(commands) == 1:
        if commands[0] == "all":
            S = (1 << 20) - 1  
            # S = 100000000000000000000 - 1 -> S = 11111111111111111111 (20 1s, each equivalent to 1~20)
        else:
            S = 0
    else:
        cmd, num = commands[0], int(commands[1])-1
        if cmd == "add":
            S |= (1 << num) # 0 -> 1, 1 -> 1
        elif cmd == "remove":
            S &= ~(1 << num) # target: 0 -> 0, 1 -> 0, rest: 0 -> 0, 1 -> 1
        elif cmd == "check":
            # if ((S & (1 << num)) >> num) == 1, does the same thing
            # ex) S = 10 (2), S & 1<<1 -> 2 (result is itself), S & 1<<2 -> 0
            if (S & (1 << num)):
                print(1)
            else: print(0)
        elif cmd == "toggle": 
            S ^= (1 << num) #target: 1->0, 0->1