def solution(n, k):
    answer = []
    
    factorial={0:1}
    temp=1
    for i in range(1,20):
        temp*=i
        factorial[i]=temp
    used=[0]*(n+1)
    
    def sol(num,depth):
        if depth==0: return
        idx=1
        temp=num
        sub=factorial[depth-1]
        while used[idx]:idx+=1
        while temp-sub>=0:
            if not used[idx]:
                temp-=sub
            idx+=1
        while used[idx]:idx+=1    
        used[idx]=1
        answer.append(idx)
        sol(temp,depth-1)
    
    sol(k-1,n)
    return answer