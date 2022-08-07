def find(a):
    if p[a]<0: return a
    else:
        p[a]=find(p[a])
        return p[a]

def union(a,b):
    a,b=find(a), find(b)
    if a!=b:
        if b in truth: p[a]=b
        elif a!=b:p[b]=a
    
n,m=map(int,input().split())
p=[-1 for i in range(n+1)]
truth=list(map(int,input().split()))[1:]
party=[list(map(int,input().split()))[1:] for i in range(m)]
for k in range(m):
    l=len(party[k])
    for i in range(l):
        for j in range(l):
            if i==j:continue
            union(party[k][i],party[k][j])
#            print(party[k][i],party[k][j],p)
     

answer=0
for x in party:
    lie=True
    for j in x:
        if find(j) in truth:
            lie=False
            break
    if lie: answer+=1
print(answer)

