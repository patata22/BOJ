def sol(now,weight):
    if weight>capa: return
    if weight==capa:
        global answer
        answer='YES'
        return
    for i in range(now+1,10):
        if not used[i]:
            used[i]=1
            sol(i,weight+potatoes[i])
            used[i]=0
    

for _ in range(int(input())):
    temp=list(map(int,input().split()))
    n=temp[0]
    capa=temp[1]
    potatoes=temp[2:]
    used=[0]*10
    answer='NO'
    sol(-1,0)
    print(n,answer)
    