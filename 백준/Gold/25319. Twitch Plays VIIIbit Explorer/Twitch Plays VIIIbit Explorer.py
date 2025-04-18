import sys
input=sys.stdin.readline

def lvUp():
    global x,y
    for z in original:
        target=ord(z)-97
        index=idx[target]
        nx,ny = location[target][index]
        move(x,y,nx,ny)
        answer.append('P')
        x,y=nx,ny
        idx[target]+=1
        
def move(x,y,nx,ny):
    if x<nx:answer.append('D'*(nx-x))
    elif x>nx: answer.append('U'*(x-nx))
    if y<ny: answer.append('R'*(ny-y))
    elif y>ny: answer.append('L'*(y-ny))

n,m,s=map(int,input().split())

location=[[] for i in range(26)]
idx=[0]*26
for i in range(n):
    temp=list(input())
    for j in range(m):
        location[ord(temp[j])-97].append((i,j))

original = list(input().rstrip())
count=[0]*26
for x in original:
    count[ord(x)-97]+=1

level=float('inf')
for i in range(26):
    if not count[i]: continue
    level=min(level,len(location[i])//count[i])

answer=[]

x,y=0,0

for _ in range(level):lvUp()

move(x,y,n-1,m-1)
answer=''.join(answer)
print(level,len(answer))
print(answer)
