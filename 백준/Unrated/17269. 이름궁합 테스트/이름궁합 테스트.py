c={}
temp=[3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
for i in range(65,91):
    c[chr(i)]=temp[i-65]
n,m=map(int,input().split())
a,b=input().split()

name=[]
nxt=[]
if n<m:
    for i in range(n):
        name.append(c[a[i]])
        name.append(c[b[i]])
    for i in range(n,m):
        name.append(c[b[i]])
else:
    for i in range(m):
        name.append(c[a[i]])
        name.append(c[b[i]])
    for i in range(m,n):
        name.append(c[a[i]])

while len(name)>2:
    for i in range(len(name)-1):
        nxt.append((name[i]+name[i+1])%10)
    name=nxt
    nxt=[]

print(int(''.join(map(str,name))),'%',sep='')