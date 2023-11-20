while True:
    n,d=map(int,input().split())
    alumni=[0]*n
    if not n: break
    answer='no'
    for _ in range(d):
        temp=list(map(int,input().split()))
        for i in range(n):
            alumni[i]+=temp[i]
    for i in range(n):
        if alumni[i]==d:answer='yes'
    print(answer)
        
    
