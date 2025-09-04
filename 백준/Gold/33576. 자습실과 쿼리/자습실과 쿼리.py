import sys
input=sys.stdin.readline

def sol(x):
    global leftFree,rightFree
    if leftFree>=x or rightFree<=x: return 0

    needLeft=leftWall[x]-leftWall[leftFree]
    needRight=rightWall[x]-rightWall[rightFree]
    if needLeft<needRight:
        leftFree=max(leftFree,x)
        return needLeft
    elif needLeft>needRight:
        rightFree=min(rightFree,x)
        return needRight
    else:
        leftDistance=x-1
        rightDistance=n-x
        if leftDistance<=rightDistance:
            leftFree=max(leftFree,x)
            return needLeft
        else:
            rightFree=min(rightFree,x)
            return needRight
    
n,m,q=map(int,input().split())

leftWall=[0]*(n+2)
rightWall=[0]*(n+2)

for _ in range(m):
    a,b=map(int,input().split())
    leftWall[a]+=b
    rightWall[a]+=b

for i in range(1,n+2):
    leftWall[i]+=leftWall[i-1]
for i in range(n,-1,-1):
    rightWall[i]+=rightWall[i+1]

leftFree=0
rightFree=n+1

for _ in range(q):
    print(sol(int(input())))
