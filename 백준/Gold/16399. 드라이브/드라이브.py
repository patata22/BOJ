C,E,D=map(int,input().split())
n=int(input())
if n==0:
    if C//E>=D: print(0)
    else: print(-1)

else:
    n+=1
    temp=[0]+list(map(int,input().split()))
    for i in range(1,n):
        temp[i]+=temp[i-1]

    station=[]
    for i in range(n):
        if temp[i]>=D: break
        station.append(temp[i])
    station.append(D)
    n=len(station)

    price=[0]+list(map(int,input().split()))
    price.append(0)

    dp=[[float('inf')]*(C+1) for i in range(n)]
    dp[0][C]=0
    for i in range(n-1):
        for j in range(C+1):
            if dp[i][j]==float('inf'): continue
            nxtDist = station[i+1]-station[i]
            oilLeft = j-nxtDist*E
            if oilLeft<0: continue
            nxtPrice=price[i+1]
            for nxtOil in range(oilLeft, C+1):
                cost=(nxtOil-oilLeft)*nxtPrice
                dp[i+1][nxtOil]=min(dp[i+1][nxtOil],dp[i][j]+cost)
    answer=min(dp[-1])
    if answer==float('inf'):
        print(-1)
    else: print(answer)
