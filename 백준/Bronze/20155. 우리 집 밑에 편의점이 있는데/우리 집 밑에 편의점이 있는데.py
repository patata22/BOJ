n,m=map(int,input().split())
count={}
answer=0
for _ in range(1,m+1):
    count[_]=0
for x in tuple(map(int,input().split())):
    count[x]+=1
    answer=max(answer,count[x])
print(answer)
