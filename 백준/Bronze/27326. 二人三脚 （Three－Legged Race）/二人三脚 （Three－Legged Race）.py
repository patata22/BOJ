count={}
for i in range(1,int(input())+1):count[i]=0
for x in map(int,input().split()):
    count[x]+=1
for x in count:
    if count[x]==1: print(x)
