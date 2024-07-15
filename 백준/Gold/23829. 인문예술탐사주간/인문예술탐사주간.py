import sys
input=sys.stdin.readline

MAX=10000001

n,q=map(int,input().split())
tree=tuple(map(int,input().split()))
left=[0]*MAX
right=[0]*MAX

for t in tree:
    left[t+1]+=1
    right[t-1]+=1
for _ in range(2):
    for i in range(1,MAX):
        left[i]+=left[i-1]
    for i in range(MAX-2,-1,-1):
        right[i]+=right[i+1]

for _ in range(q):
    n=int(input())
    print(left[n]+right[n])
    
    
