import sys
input=sys.stdin.readline
X=[]
Y=[]
n=int(input())
for _ in range(n):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
mx = X[n//2]
my = Y[n//2]
answer=0
for x in X:answer+=abs(x-mx)
for y in Y:answer+=abs(y-my)
print(answer)