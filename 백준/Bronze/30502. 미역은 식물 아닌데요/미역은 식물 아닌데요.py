n,m=map(int,input().split())

move=[-1]*(n+1)
light=[-1]*(n+1)

for _ in range(m):
    a,b,c=input().split()
    a,c=int(a),int(c)
    if b=='P':light[a]=c
    else: move[a]=c

a1=0
a2=0
for i in range(1,n+1):
    if move[i]<0 and light[i]<0:  a2+=1
    elif move[i]<0 and light[i]==1: a2+=1
    elif move[i]==0 and light[i]<0: a2+=1
    elif move[i]==0 and light[i]==1:
        a1+=1
        a2+=1
print(a1,a2)
