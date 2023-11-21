import sys
input=sys.stdin.readline

mini=float('inf')
maxi=0
total=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    t=a/b
    total+=t
    mini=min(mini,t)
    maxi=max(maxi,t)
print(mini,maxi,total)
    
