def sol(depth):
    if depth==n:        
        global answer
        cnt=0
        for i in range(n):
            if S[i]<=0: cnt+=1
        answer=max(answer,cnt)
        return
    B=False
    if S[depth]<=0: sol(depth+1)
    
    else:
        s,w=S[depth],W[depth]
        for i in range(n):
            if i==depth or S[i]<=0: continue
            B=True
            S[i]-=w
            S[depth]-=W[i]
            sol(depth+1)
            S[depth]+=W[i]
            S[i]+=w
        if not B: sol(depth+1)
        

n=int(input())
S=[]
W=[]
for _ in range(n):
    a,b=map(int,input().split())
    S.append(a)
    W.append(b)

answer=0
sol(0)
print(answer)
