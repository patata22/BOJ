d=((1,3,9),(1,9,3),(3,1,9),(3,9,1),(9,1,3),(9,3,1))
def s(x,y,z):
    if x+y+z==0:return 0
    if p[x][y][z]==61:
        for a,b,c in d:
            e,f,g=max(0,x-a),max(0,y-b),max(0,z-c)
            p[x][y][z]=min(p[x][y][z],s(e,f,g)+1)
    return p[x][y][z]
n=int(input())
h=list(map(int,input().split()))+[0]*(3-n)
p=[[[61]*61 for i in range(61)] for i in range(61)]
print(s(*h))