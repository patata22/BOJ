n,m,a=map(int,input().split())
answer=0
number=list(map(int,input().split()))
for i in range(0,n*m-m,m):
    for j in range(i,i+m):
        if number[j]*2<number[j+m]:answer+=1
print(answer*a)
