def sol(depth,now):
    if depth==n-2:
        global answer
        answer=max(answer,now)
        return
    for i in range(1,n-1):
        if not used[i]:
            used[i]=1
            l=i-1
            r=i+1
            while used[l]:l-=1
            while used[r]:r+=1
            sol(depth+1, now+energy[l]*energy[r])
            used[i]=0
            
        
n=int(input())
energy=tuple(map(int,input().split()))
used=[0]*n
answer=0

sol(0,0)
print(answer)