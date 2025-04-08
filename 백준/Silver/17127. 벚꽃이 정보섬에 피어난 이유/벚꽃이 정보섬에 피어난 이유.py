n=int(input())
number=list(map(int,input().split()))
answer=0

for i in range(1,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            result=0
            temp=1
            for x in range(i):
                temp*=number[x]
            result+=temp
            temp=1
            for x in range(i,j):
                temp*=number[x]
            result+=temp
            temp=1
            for x in range(j,k):
                temp*=number[x]
            result+=temp
            temp=1
            for x in range(k,n):
                temp*=number[x]
            result+=temp
            answer=max(answer,result)
print(answer)