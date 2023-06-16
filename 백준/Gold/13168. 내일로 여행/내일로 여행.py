n,r=map(int,input().split())

stationNo={}
for i,x in enumerate(input().split()):
    stationNo[x]=i

m=int(input())
city=input().split()

naeil={}
naeil['Mugunghwa']=0
naeil['ITX-Saemaeul']=0
naeil['ITX-Cheongchun']=0
naeil['S-Train']=0.5
naeil['V-Train']=0.5
naeil['KTX']=1
naeil['Subway']=1
naeil['Bus']=1
naeil['Taxi']=1
naeil['Airplane']=1

distance=[[float('inf')]*n for i in range(n)]

ticket=[input().split() for i in range(int(input()))]

for t, s, e, p in ticket:
    s,e=stationNo[s],stationNo[e]
    distance[s][e]=min(distance[s][e],int(p))
    distance[e][s]=distance[s][e]

for k in range(n):
    distance[k][k]=0
    for i in range(n):
        for j in range(n):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]

price=0
for i in range(m-1):
    price+=distance[stationNo[city[i]]][stationNo[city[i+1]]]

distance=[[float('inf')]*n for i in range(n)]
for t, s, e, p in ticket:
    s,e=stationNo[s],stationNo[e]
    distance[s][e]=min(distance[s][e],naeil[t]*int(p))
    distance[e][s]=distance[s][e]
for k in range(n):
    distance[k][k]=0
    for i in range(n):
        for j in range(n):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]
priceNaeil=r
for i in range(m-1):
    priceNaeil+=distance[stationNo[city[i]]][stationNo[city[i+1]]]

print('Yes') if priceNaeil<price else print('No')