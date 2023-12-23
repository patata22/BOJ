while True:
    n,m=map(int,input().split())
    if n==0: break
    count=[0]*(n+1)
    for x in map(int,input().split()):
        count[x]+=1
    answer=0
    for x in count:
        if x>1:answer+=1
    print(answer)
