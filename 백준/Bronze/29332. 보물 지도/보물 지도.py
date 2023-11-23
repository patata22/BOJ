import sys
input=sys.stdin.readline

xmin,ymin=-float('inf'),-float('inf')
xmax,ymax=float('inf'),float('inf')

for _ in range(int(input())):
    x,y,c=input().rstrip().split()
    x=int(x)
    y=int(y)
    if c=='L': xmax=min(xmax,x-1)
    elif c=='R': xmin=max(xmin,x+1)
    elif c=='U': ymin=max(ymin,y+1)
    elif c=='D': ymax=min(ymax,y-1)
    
answer=(xmax-xmin+1)*(ymax-ymin+1)
if answer==float('inf'):print('Infinity')
else:print(answer)
