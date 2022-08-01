#1803

from collections import deque

def sol():
    q=deque()
    for i in range(1,n+1):
        if indegreeL[i]==0:
            answerL[i]=1
            q.append((i,0)) #0 = L 1=R
    for i in range(1,m+1):
        if indegreeR[i]==0:
            answerR[i]=1
            q.append((i,1))
    while q:
        now,side=q.popleft()
        if side==0:
            temp=shotR[shotL[now]]
            if not checkR[shotL[now]]:
                checkR[shotL[now]]=1
                indegreeL[temp]-=1
                if indegreeL[temp]==0:
                    answerL[temp]=1
                    q.append((temp,0))
        elif side==1:
            temp=shotL[shotR[now]]
            if not checkL[shotR[now]]:
                checkL[shotR[now]]=1
                indegreeR[temp]-=1
                if indegreeR[temp]==0:
                    answerR[temp]=1
                    q.append((temp,1))
    
n,m=map(int,input().split())

indegreeL=[0]*(n+1)
indegreeR=[0]*(m+1)
checkL=[0]*(n+1)
checkR=[0]*(m+1)
shotL = [0]+list(map(int,input().split()))
for i in range(1,n+1):indegreeR[shotL[i]]+=1
shotR = [0]+list(map(int,input().split()))
for i in range(1,m+1):indegreeL[shotR[i]]+=1
answerL=[0]*(n+1)
answerR=[0]*(m+1)
sol()
print(*answerL[1:],sep='')
print(*answerR[1:],sep='')
