import heapq

def sol():
    q=[]
    q.append((0,0))
    distance[0]=0
    while q:
        time, now =heapq.heappop(q)
        if distance[now]!=time: continue
        if now==n+1: return time
        for to, t in graph[now]:
            if distance[to]>time+t:
                distance[to]=time+t
                prev[to]=now
                heapq.heappush(q,(time+t, to))
                


maxdist=int(input())
n=int(input())
temp=[0]+list(map(int,input().split()))
for i in range(1,n+2): temp[i]+=temp[i-1]
graph=[[] for i in range(n+2)]
time=[0]+list(map(int,input().split()))+[0]
for i in range(n+2):
    for j in range(i+1,n+2):
        dist=temp[j]-temp[i]
        if dist<=maxdist:
            graph[i].append((j,time[j]))
            graph[j].append((i,time[i]))


distance=[float('inf')]*(n+2)
prev=[-1]*(n+2)

print(sol())

now=n+1
count=0
station=[]
while prev[now]!=0:
    count+=1
    now=prev[now]
    station.append(now)
print(count)
print(*station[::-1])

