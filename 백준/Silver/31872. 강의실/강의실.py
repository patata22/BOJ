n,k=map(int,input().split())

location=[0]+list(map(int,input().split()))
location.sort()
gap=[]
answer=0
for i in range(1,n+1):
    temp=location[i]-location[i-1]
    answer+=temp
    gap.append(temp)
gap.sort()
for _ in range(k):
    answer-=gap.pop()

print(answer)
