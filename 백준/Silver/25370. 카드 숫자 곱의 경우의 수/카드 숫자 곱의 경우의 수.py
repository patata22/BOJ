def sol(now, count, total):
    if count==n:
        answer.add(total)
        return
    for i in range(now, 10):
        sol(i,count+1,total*i)


n=int(input())
answer=set()
sol(1,0,1)
print(len(answer))
