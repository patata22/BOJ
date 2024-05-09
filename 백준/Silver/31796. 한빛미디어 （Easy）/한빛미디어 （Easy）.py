n=int(input())
book=sorted(list(map(int,input().split())))
answer=1
now=book[0]
for i in range(1,n):
    if book[i]>=2*now:
        now=book[i]
        answer+=1
print(answer)
