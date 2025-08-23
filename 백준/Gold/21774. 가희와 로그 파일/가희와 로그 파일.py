import sys
input=sys.stdin.readline

def parseYMD(x):
    y,m,d=map(int,x.split('-'))
    return (10000*y+100*m+d)*100000
    
def parseHMS(x):
    h,m,s=map(int,x.split(':'))
    return 3600*h+60*m+s

def parseTime(T):
    ymd,hms=T.split()
    return parseYMD(ymd)+parseHMS(hms)

def parseLog(log):
    time,level=log.split('#')
    return (parseTime(time),int(level))

def parseQuery(query):
    temp=query.split('#')
    start,end,level=parseTime(temp[0]),parseTime(temp[1]),int(temp[2])
    s=findStart(start)
    e=findEnd(end)

    return (dp[e][6]-dp[e][level-1])-(dp[s][6]-dp[s][level-1])

def findStart(T):
    l=0
    r=len(time)
    while l+1<r:
        mid=(l+r)//2
        if time[mid]<T: l=mid
        else: r=mid
    return change[time[l]]    

def findEnd(T):
    l=-1
    r=len(time)
    while l+1<r:
        mid=(l+r)//2
        if time[mid]<=T: l=mid
        else: r=mid
    return change[time[l]]

n,q=map(int,input().split())

logs=[parseLog(input()) for i in range(n)]
logs.sort(key=lambda x: x[0])

time=[0]
change={}
change[0]=0
unused=1

for log in logs:
    t = log[0]
    if t not in change:
        change[t]=unused
        unused+=1
        time.append(t)
    
dp=[[0]*7 for i in range(unused)]

for log in logs:
    t=change[log[0]]
    l=log[1]
    dp[t][l]+=1

for i in range(1,unused):
    for j in range(1,7):
        dp[i][j]+=dp[i][j-1]

for j in range(1,7):
    for i in range(1,unused):
        dp[i][j]+=dp[i-1][j]

for _ in range(q):
    print(parseQuery(input()))
