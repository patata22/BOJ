import sys
input=sys.stdin.readline
n=int(input())
sx,sy=map(int,input().split())
for _ in range(n-2): input()
ex,ey=map(int,input().split())
print(((sx-ex)**2+(sy-ey)**2)**0.5)
