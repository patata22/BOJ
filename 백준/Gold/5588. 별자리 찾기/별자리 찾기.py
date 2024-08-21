import sys
input=sys.stdin.readline

def sol():
    for x,y in star:
        flag=True
        for dx,dy in diff:
            if (x+dx, y+dy) not in star:
                flag=False
                break
        if not flag: continue
        return [x,y]
        

m=int(input())
original=[tuple(map(int,input().split())) for i in range(m)]
original.sort()
ox,oy=original[0]
diff=[]
for i in range(1,m):
    x,y=original[i]
    diff.append((x-ox, y-oy))
n=int(input())
star=set()
for i in range(n):
    star.add(tuple(map(int,input().split())))
x,y=sol()
print(x-ox,y-oy)
