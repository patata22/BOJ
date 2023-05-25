import sys
input=sys.stdin.readline

def sol():
    fun=0
    for a,b in positive:
        if a>fun:
            return 0
        fun+=b-a
    for a,b in negative:
        if a>fun:
            return 0
        fun+=b-a
    return 1

n=int(input())
positive=[]
negative=[]
for _ in range(n):
    a,b=map(int,input().split())
    if a>=b:
        negative.append((a,b))
    else:positive.append((a,b))
positive.sort(key=lambda x: (x[0],-(x[1]-x[0])))
negative.sort(key=lambda x: x[1], reverse=True)

print(sol())
