def sol():
    cnt=0
    for i in range(n-1,0,-1):
        for j in range(i):
            now=number[j]
            nxt=number[j+1]
            if now>nxt:
                cnt+=1
                if cnt==k: return (nxt,now)
                number[j]=nxt
                number[j+1]=now
    return [-1]
            

n,k=map(int,input().split())
number=list(map(int,input().split()))

print(*sol())
