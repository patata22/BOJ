import sys
input=sys.stdin.readline

def sol():
    now=0
    for start, t in time:
        if start-now>=m:
            return now
        now=start+t
    if s-now>=m: return now
    return -1
        

n,m,s=map(int,input().split())
time=[tuple(map(int,input().split())) for i in range(n)]
time.sort()
print(sol())
