for _ in range(int(input())):
    n,m,l=map(int,input().split())
    l-=1
    answer=0
    for i in range(n):
        if l==0: answer+=1
        l=(l+1)%m
    print(answer)
    
