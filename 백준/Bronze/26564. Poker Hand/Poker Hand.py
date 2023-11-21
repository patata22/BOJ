for _ in range(int(input())):
    count={}
    for i in range(2,10):count[str(i)]=0
    for i in ('A','T','J','Q','K'): count[i]=0
    temp=input().split()
    for x in temp:
        count[x[0]]+=1
    answer=0
    for x in count: answer=max(answer,count[x])
    print(answer)

