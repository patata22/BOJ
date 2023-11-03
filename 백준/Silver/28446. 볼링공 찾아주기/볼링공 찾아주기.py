import sys
input=sys.stdin.readline

locker={}
for _ in range(int(input())):
    temp=list(map(int,input().split()))
    a=temp[0]
    if a==1: locker[temp[2]]=temp[1]
    else: print(locker[temp[1]])
