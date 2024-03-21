import sys
input=sys.stdin.readline

def sol():
    L=car[s]-fuel[s]
    R=car[s]+fuel[s]
    l=s-1
    r=s+1
    flag=1
    while flag:
        flag=0
        if r<n and car[r]<=R:
            R=max(R,car[r]+fuel[r])
            L=min(L,car[r]-fuel[r])
            flag=1
            answer.append(r+1)
            r+=1
        if l>=0 and car[l]>=L:
            R=max(R,car[l]+fuel[l])
            L=min(L,car[l]-fuel[l])
            flag=1
            answer.append(l+1)
            l-=1
    
n,s=map(int,input().split())
s-=1
car=tuple(map(int,input().split()))
fuel=tuple(map(int,input().split()))
L=car[s]-fuel[s]
R=car[s]+fuel[s]

answer=[]
answer.append(s+1)
sol()
answer.sort()
print(*answer)

