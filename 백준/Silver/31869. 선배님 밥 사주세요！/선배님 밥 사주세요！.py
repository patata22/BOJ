promise={}

able=[0]*70

n=int(input())
for _ in range(n):
    name, week, day, m = input().split()
    promise[name]=(int(week),int(day),int(m))

for _ in range(n):
    name,m = input().split()
    m=int(m)
    w,d,M = promise[name]
    if M<=m: able[7*(w-1)+d]=1
    
answer=0
cnt=0
for i in range(70):
    if able[i]:
        cnt+=1
    else:
        answer=max(cnt,answer)
        cnt=0
answer=max(cnt,answer)

print(answer)
