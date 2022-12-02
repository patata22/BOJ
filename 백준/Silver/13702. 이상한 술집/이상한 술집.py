import sys
input=sys.stdin.readline

def search(mid):
    count = 0
    for x in drink:
        count+=x//mid
    return count>=k
    

n,k = map(int,input().split())

drink = [int(input()) for i in range(n)]

l=0
r=2**31-1

while l+1<r:
    mid = (l+r)//2
    if search(mid): l=mid
    else: r=mid
print(l)
    
