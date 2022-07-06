import sys
input=sys.stdin.readline

def check(mid):
    global success
    temp=0
    for x in kim:
        if x<2*k:
            if x-k>=mid:
                temp+= (x-k)//mid
        else:
            if x-2*k>=mid:
                temp+=(x-2*k)//mid
                
    if temp>=m:
        success=True
        return True
    else:return False
        


n,k,m=map(int,input().split())
kim=[]
for _ in range(n):
    x=int(input())
    if x>k:kim.append(x)

success=False

l=0
r=10**9+1
while l+1<r:
    mid=(l+r)//2
    if check(mid):l=mid
    else:r=mid
print(l) if success else print(-1)
