time=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    if b: time.append(a)
answer=0
for i in range(1,len(time)):
    answer=max(time[i]-time[i-1],answer)
print(answer)
