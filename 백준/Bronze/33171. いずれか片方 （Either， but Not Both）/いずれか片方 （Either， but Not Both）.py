n=int(input())
answer=0
a,b=int(input()),int(input())
for i in range(1,n+1):
    if (i%a==0 and i%b) or (i%b==0 and i%a): answer+=1
print(answer)