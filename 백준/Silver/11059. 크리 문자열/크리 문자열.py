number=list(map(int,input()))
n=len(number)
length=0

dp=[0]*(n+1)
for i in range(1,n+1):
    dp[i]+=dp[i-1]+number[i-1]

for i in range(n):
    for j in range(i+1,n):
        l=j-i+1
        if l%2: continue
        mid=i+l//2
        left=dp[mid]-dp[i]
        right=dp[j+1]-dp[mid]
        
        if left==right: length=max(length,l)

print(length)