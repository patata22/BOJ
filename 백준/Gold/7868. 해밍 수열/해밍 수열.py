p1,p2,p3,n=map(int,input().split())
answer=set()
for i in range(61):
    for j in range(61):
        for k in range(61):
            answer.add((p1**i)*(p2**j)*(p3**k))
            answer.add((p1**i)*(p3**j)*(p2**k))
            answer.add((p2**i)*(p1**j)*(p3**k))
            answer.add((p2**i)*(p3**j)*(p1**k))
            answer.add((p3**i)*(p1**j)*(p2**k))
            answer.add((p3**i)*(p2**j)*(p1**i))
answer=sorted(list(answer))
print(answer[n])
