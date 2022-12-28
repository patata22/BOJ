import sys
input=sys.stdin.readline

def lower_bound(i):
    l=-1
    r=n
    while l+1<r:
        mid = (l+r)//2
        if not point_x[mid]>=i:l=mid
        else: r= mid
    return point_y[r-1]
def upper_bound(i):
    l=-1
    r=n
    while l+1<r:
        mid = (l+r)//2
        if not point_x[mid]>i: l=mid
        else: r = mid
    return point_y[r]

point_x = []
point_y = []

n=int(input())
for _ in range(n):
    x,y= map(int,input().split())
    point_x.append(x)
    point_y.append(y)

for _ in range(int(input())):
    x=float(input())
    y1 = lower_bound(x)
    y2 = upper_bound(x)
    
    if y1>y2:print(-1)
    elif y1<y2:print(1)
    else:print(0)