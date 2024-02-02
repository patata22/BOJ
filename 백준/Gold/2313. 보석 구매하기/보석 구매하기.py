import sys
input=sys.stdin.readline

V=0
answer=[]

for _ in range(int(input())):
    n=int(input())
    number=list(map(int,input().split()))
    l=0
    L,R=0,0
    value=-float('inf')
    temp=0
    for i in range(n):
        curr= number[i]
        temp+=curr
        if curr>=temp:
            temp=curr
            l=i
        if temp>value:
            value=temp
            L,R=l,i
        elif temp==value:
            if R-L>i-l:
                L,R=l,i
    V+=value
    answer.append((L+1,R+1))
print(V)
for x in answer:
    print(*x) 