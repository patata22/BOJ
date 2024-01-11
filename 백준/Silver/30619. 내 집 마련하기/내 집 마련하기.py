n=int(input())
number=list(map(int,input().split()))
for _ in range(int(input())):
    answer=number[:]
    l,r=map(int,input().split())
    now=l
    for i in range(n):
        if l<=answer[i]<=r:
            answer[i]=now
            now+=1
    print(*answer)
