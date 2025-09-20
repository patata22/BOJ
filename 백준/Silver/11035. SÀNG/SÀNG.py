def sol():
    n,k=map(int,input().split())
    isPrime=[1]*(n+1)
    cnt=0
    for i in range(2,n+1):
        if isPrime[i]:
            for j in range(i,n+1,i):
                if isPrime[j]:
                    cnt+=1
                    isPrime[j]=0
                    if cnt==k: return j
    
while True:
    try: print(sol())
    except EOFError: break