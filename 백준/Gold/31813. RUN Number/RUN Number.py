def makeNum(i,n):
    return int(str(i)*n)

for tt in range(int(input())):
    n,k=map(int,input().split())
    answer=[]
    for i in range(n):
        if k==10:
            answer.append(9)
            answer.append(1)
            break
        now=k//(10**(n-i-1))
        temp=makeNum(now,n-i)
        if temp<=k:
            if temp: answer.append(temp)
            k-=temp
        else:
            temp=makeNum(now-1,n-i)
            k-=temp
            if temp: answer.append(temp)
            
        if not k: break
    print(len(answer))
    print(*answer)

