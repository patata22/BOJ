import sys
input=sys.stdin.readline

V=0
answer=[]

for _ in range(int(input())):
    n=int(input())
    number=[0]+list(map(int,input().split()))
    for i in range(1,n+1):
        number[i]+=number[i-1]
    l=0
    r=0
    value=-float('inf')
    for i in range(1,n+1):
        for j in range(1,i+1):
            temp=number[i]-number[j-1]
            if temp>value:
                value=temp
                l,r=j,i
            elif temp==value and r-l>i-j:
                l,r=j,i
                
    V+=value
    answer.append((l,r))

print(V)
for x in answer:print(*x)
                
