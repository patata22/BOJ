import sys
input=sys.stdin.readline

def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

gap=[]
n=int(input())
tree=[]
before=int(input())
tree.append(before)
for _ in range(n-1):
    now=int(input())
    tree.append(now)
    gap.append(now-before)
    before=now

while len(gap)>1:
    gap.append(gcd(gap.pop(),gap.pop()))

answer=0
dist=gap[0]

for i in range(1,n):
    temp=tree[i]-tree[i-1]
    answer+=(temp//dist-1)
print(answer)
