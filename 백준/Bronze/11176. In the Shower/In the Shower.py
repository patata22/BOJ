for _ in range(int(input())):
    e,n=map(int,input().split())
    answer=0
    for __ in range(n):
        if int(input())>e:answer+=1
    print(answer)
