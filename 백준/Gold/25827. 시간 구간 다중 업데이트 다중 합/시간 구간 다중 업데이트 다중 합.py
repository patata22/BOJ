import sys
input=sys.stdin.readline

def parseTime(x):
    h,m,s=x.split(':')
    return 3600*int(h)+60*int(m)+int(s)

n=int(input())
time=[0]*86400

query=[]
for _ in range(n):
    a,b,c=input().split()
    b,c=parseTime(b), parseTime(c)
    if a=='1':
        time[b]+=1
        time[c]-=1
    else:
        query.append((b,c))

for i in range(1,86400):
    time[i]+=time[i-1]

for i in range(1,86400):
    time[i]+=time[i-1]

for s,e in query:
    if s==0: print(time[e-1])
    else: print(time[e-1]-time[s-1])
