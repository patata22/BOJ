import sys
input=sys.stdin.readline
n=int(input())
lst1=list(map(int,input().split()))
counted=[0 for i in range(20000001)]
for x in lst1:
    counted[x+10000000]+=1
m=int(input())
lst2=list(map(int,input().split()))
for x in lst2:
    print(counted[x+10000000],end=' ')