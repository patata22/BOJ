n,m,k,a,b,c=map(int,input().split())
x=[(a*n,'Joffrey'), (b*m, 'Robb'), (c*k, 'Stannis')]
x.sort(key=lambda x: x[1])
M=max(a*n, b*m, c*k)
answer=[]
for n,name in x:
    if n==M:answer.append(name)

print(*answer)
