n,m=map(int,input().split())
answer=0
while n!=m:
    answer+=1
    if n*2<=m and m%2==0: m//=2
    else: m-=1
print(answer)
    
