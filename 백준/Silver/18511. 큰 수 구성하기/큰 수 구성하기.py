def sol(depth):
    global answer
    if depth==N:
        return
    for x in number:
        temp.append(x)
        x=int(''.join(temp))
        if x<=n: answer=max(answer,x)
        sol(depth+1)
        temp.pop()
    
n,k=map(int,input().split())
N=len(str(n))
number=input().split()

answer=0
temp=[]

sol(0)
print(answer)
