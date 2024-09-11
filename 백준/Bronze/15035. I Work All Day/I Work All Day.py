n=int(input())
h=map(int,input().split())
t=int(input())
waste=float('inf')
for x in h:
    if t%x<waste:
        waste=t%x
        answer=x
print(answer)