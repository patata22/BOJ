def sol(x,idx1,idx2):
    l=0
    r=L
    temp=(idx1,idx2)
    while l+1<r:
        mid=(l+r)//2
        if comb[mid][0]<=x: l=mid
        else: r=mid
    if l>=0:
        while comb[l][1] in temp or comb[l][2] in temp:
            l-=1
            if l<0: break
    if r<L:
        while comb[r][1] in temp or comb[r][2] in temp:
            r+=1
            if r>=L: break
    result=float('inf')
    if l>=0: result=min(result,x-comb[l][0])
    if r<L: result=min(result, comb[r][0]-x)
    return result
    


n=int(input())
number=list(map(int,input().split()))
comb=[]
for i in range(n):
    for j in range(i+1,n):
        comb.append((number[i]+number[j],i,j))
L=len(comb)
comb.sort()

answer=float('inf')
for x,i,j in comb:
    answer=min(answer,sol(x,i,j))

print(answer)
