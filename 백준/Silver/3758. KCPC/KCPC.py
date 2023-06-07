import sys
input=sys.stdin.readline

for T in range(int(input())):
    n,k,t,m=map(int,input().split())
    submit={}
    time={}
    score=[{} for i in range(n+1)]
    for i in range(1,n+1):
        submit[i]=0
        time[i]=0
    for _ in range(m):
        i,j,s=map(int,input().split())
        submit[i]+=1
        time[i]=_
        if j not in score[i]:score[i][j]=s
        else:score[i][j]=max(score[i][j],s)
    result=[]
    for i in range(1,n+1):
        total=0
        for x in score[i]:
            total+=score[i][x]
        result.append((-total, submit[i], time[i],i))
    result.sort()
    for i in range(1,n+1):
        if result[i-1][3]==t:
            print(i)
            break
        
