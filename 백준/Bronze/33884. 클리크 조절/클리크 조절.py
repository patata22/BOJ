import sys
input=sys.stdin.readline

n=int(input())
original=sorted([tuple(map(int,input().split())) for i in range(n)])
nxt=sorted([tuple(map(int,input().split())) for i in range(n)])
x1,y1=original[0]
x2,y2=nxt[0]
print(x2-x1,y2-y1)
                
