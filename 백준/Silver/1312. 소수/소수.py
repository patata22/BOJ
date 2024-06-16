
a,b,n=map(int,input().split())
a=(a%b)*10
answer=a
for _ in range(n):
    answer=a//b
    a=(a%b)*10
print(answer)
    
        
