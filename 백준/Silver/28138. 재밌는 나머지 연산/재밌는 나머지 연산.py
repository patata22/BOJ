n,r=map(int,input().split())
n-=r
answer=0
temp=int(n**0.5)
for i in range(1,temp+1):
    if n%i==0:
        if i>r: answer+=i
        if n//i>r: answer+=n//i
        if i>r and i==n//i:answer-=i
    
print(answer)
    
    
