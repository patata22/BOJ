import sys
input=sys.stdin.readline
count=[0 for i in range(20000001)]
n=int(input())
lst1=list(map(int,input().split()))
for x in lst1:
    count[x+10000000]+=1
m=int(input())
lst2=list(map(int,input().split()))
for y in lst2:
    print(count[y+10000000], end=' ')
