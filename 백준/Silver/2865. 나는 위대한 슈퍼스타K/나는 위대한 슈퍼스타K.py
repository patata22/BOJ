score={}
n,m,k=map(int,input().split())
for i in range(1,n+1): score[i]=0
for _ in range(m):
    temp=list(map(float,input().split()))
    for i in range(0,len(temp),2):
        score[temp[i]]=max(score[temp[i]],temp[i+1])

temp=[]
answer=0
for x in score: temp.append(score[x])
temp.sort()
for _ in range(k):
    answer+=temp.pop()
print(round(answer+0.0001, 1))
    

    