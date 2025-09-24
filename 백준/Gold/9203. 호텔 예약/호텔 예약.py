import sys
input=sys.stdin.readline

def parseDate(x):
    y,m,d=map(int,x.split('-'))
    if y==2016:return (365*(y-2013)+month2[m-1]+d)*1440
    return (365*(y-2013)+month[m-1]+d)*1440

def parseTime(x):
    h,m=map(int,x.split(':'))
    return 60*h+m

month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
month2=month[:]
month2[2]=29
for i in range(1,12):
    month[i]+=month[i-1]
    month2[i]+=month2[i-1]

for tt in range(int(input())):
    b,c=map(int,input().split())
    unused=0
    change={}
    time=[]
    reservation=[]
    for _ in range(b):
        __,sd,st,ed,et=input().split()
        start=parseDate(sd)+parseTime(st)
        end=parseDate(ed)+parseTime(et)+c
        time.append(start)
        time.append(end)
        reservation.append((start,end))
    time.sort()
    for x in time:
        if x not in change:
            change[x]=unused
            unused+=1

    prefix=[0]*(unused+1)
    for s,e in reservation:
        prefix[change[s]]+=1
        prefix[change[e]]-=1
    for i in range(1,unused+1):
        prefix[i]+=prefix[i-1]
    print(max(prefix))