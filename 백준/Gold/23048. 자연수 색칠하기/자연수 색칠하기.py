n=int(input())
isPrime=[1]*(n+1)
color=[1]*(n+1)
C=1
for i in range(2,n+1):
    if isPrime[i]:
        C+=1
        color[i]=C
        for j in range(i+i,n+1,i):
            isPrime[j]=0
            color[j]=C
print(C)
print(*color[1:])