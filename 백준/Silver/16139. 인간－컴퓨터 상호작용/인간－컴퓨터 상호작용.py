import sys
input=sys.stdin.readline

word=input().rstrip()
l=len(word)
dp=[[0]*26 for i in range(l)]
for i in range(l):
    for j in range(26):dp[i][j]=dp[i-1][j]
    now=ord(word[i])-97
    dp[i][now]+=1

for _ in range(int(input())):
    a,b,c=input().rstrip().split()
    a=ord(a)-97
    b,c=int(b),int(c)
    print(dp[c][a]-dp[b-1][a]) if b!=0 else print(dp[c][a])
    

