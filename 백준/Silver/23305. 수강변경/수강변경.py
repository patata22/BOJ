n=int(input())
count1=[0]*1000001
count2=[0]*1000001
for x in map(int,input().split()):
    count1[x]+=1
for x in map(int,input().split()):
    count2[x]+=1
answer=0
for i in range(1,1000001): answer+=max(0,count2[i]-count1[i])
print(answer)