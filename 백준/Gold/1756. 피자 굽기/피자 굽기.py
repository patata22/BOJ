def sol():
    height=0
    for x in pizza:
        if not oven: return 0
        while oven[-1]<x:
            oven.pop()
            height+=1
            if not oven: return 0
        oven.pop()
        height+=1
    return d-height+1
        
        

d,n=map(int,input().split())

oven=list(map(int,input().split()))
for i in range(1,d):
    oven[i]=min(oven[i],oven[i-1])
pizza = list(map(int,input().split()))    
print(sol())
