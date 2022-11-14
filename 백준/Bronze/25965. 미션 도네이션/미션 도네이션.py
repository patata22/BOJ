for _ in range(int(input())):
    temp=[]
    for __ in range(int(input())):
        temp.append((tuple(map(int,input().split()))))
    k,d,A=map(int,input().split())
    answer=0
    for a,b,c in temp:
        answer+=max(0,k*a-b*d+A*c)
    print(answer)
