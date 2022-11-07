n,m=map(int,input().split())
hole = list(map(int,input().split()))
answer=0
l=0
r=1
total = hole[0]
while r<n:
        total+=hole[r]
        r+=1
        while total>m:
            total-=hole[l]
            l+=1            
        answer=max(answer,total)
print(answer)
