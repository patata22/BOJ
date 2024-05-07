n,l,d=map(int,input().split())
able=[1]*5000
now=0
for _ in range(n):
    for __ in range(l):
        able[now]=0
        now+=1
    now+=5

for i in range(0,5000,d):
    if able[i]:
        print(i)
        break
        
