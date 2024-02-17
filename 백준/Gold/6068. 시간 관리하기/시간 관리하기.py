n=int(input())
work=[tuple(map(int,input().split())) for i in range(n)]
work.sort(key=lambda x: x[1])
answer=float('inf')
while work:
    t,s=work.pop()
    answer=min(answer,s)-t
if answer<0:print(-1)
else:print(answer)
