import sys
input=sys.stdin.readline

for t in range(int(input())):
    n,m,k=map(int,input().split())
    temp = list(map(int,input().split()))
    if n==m:
        if sum(temp)<k: print(1)
        else: print(0)
    else:
        home = temp+temp
        total = sum(home[:m])
        l=0
        answer= 0
        if total <k : answer+=1
        while l<n-1:
            l+=1
            r=l+m-1
            total +=home[r]-home[l-1]
            if total<k:
                answer+=1
        print(answer)