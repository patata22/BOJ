def sol(x,y):
    if y==0: return 0
    l=0
    r=10**9+1
    while l+1<r:
        mid=(l+r)//2
        if check(mid,x,y): r=mid
        else:l=mid
    return r

def check(mid,x,y):
    if x==1: return True
    total=mid
    while mid>=x:
        temp=mid//x+mid%x
        total+=mid//x
        mid=temp
    
    return total>=y


m=int(input())
N=tuple(map(int,input().split()))
target=tuple(map(int,input().split()))
answer=[]
for i in range(m):
    answer.append(sol(N[i],target[i]))

print(*answer)
