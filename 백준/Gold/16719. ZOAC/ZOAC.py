def sol(depth):
    if depth==n:
        return
    cand=[]
    for i in range(n):
        if not used[i]:  
            temp=[]
            for j in range(i):
                if used[j]: temp.append(word[j])
            temp.append(word[i])
            for j in range(i+1,n):
                if used[j]: temp.append(word[j])
            cand.append((temp,i))
    cand.sort()
    x,i=cand[0]
    used[i]=1
    print(''.join(x))
    sol(depth+1)

word=list(input())
n=len(word)
used=[0]*n
sol(0)
