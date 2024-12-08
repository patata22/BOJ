n,a,b=map(int,input().split())
answer=[0]*3
for i in range(1,n+1):
    if not i%a and not i%b: answer[2]+=1
    elif not i%a: answer[0]+=1
    elif not i%b: answer[1]+=1
print(*answer)
