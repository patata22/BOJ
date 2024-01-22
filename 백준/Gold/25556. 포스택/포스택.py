n=int(input())
number=list(map(int,input().split()))

answer='YES'
stack=[[0] for i in range(4)]
for i in range(n):
    now=number[i]
    temp=[(stack[i][-1],i) for i in range(4)]
    temp.sort(key=lambda x: -x[0])
    flag=0
    for a,b in temp:
        if a<now:
            stack[b].append(now)
            flag=1
            break
    if not flag:answer='NO'
print(answer)