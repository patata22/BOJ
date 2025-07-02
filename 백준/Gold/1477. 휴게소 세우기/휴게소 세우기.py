def sol():
    l=0
    r=L
    while l+1<r:
        mid=(l+r)//2
        if check(mid): r=mid
        else: l=mid
    return r

def check(mid):
    now=0
    cnt=0
    idx=1
    while now+mid<L:
        if now+mid>=number[idx]:
            now=number[idx]
            idx+=1
        else:
            now=now+mid
            cnt+=1
    if cnt>m: return False
    return True

n,m,L=map(int,input().split())
number=[0]
if n: number+=list(map(int,input().split()))
number.sort()
number.append(L)
n+=2
print(sol())
