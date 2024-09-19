for tt in range(int(input())):
    count={}
    n,X=map(int,input().split())
    for x in map(int,input().split()):
        if x not in count:count[x]=0
        count[x]+=1
    answer=0
    for x in count:
        if X^x==x: answer+=(count[x]*(count[x]-1))
        elif X^x in count:
            answer+=(count[x]*count[X^x])
    print(answer//2)
