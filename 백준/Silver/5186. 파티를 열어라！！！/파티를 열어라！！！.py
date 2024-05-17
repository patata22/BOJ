for tt in range(int(input())):
    n,c,l=map(int,input().split())
    moveable=[0]*(l+1)
    member=[0]*(l+1)
    seat=[[] for i in range(n+1)]
    total=0
    for _ in range(n):
        a,b=input().split()
        a=int(a)
        if b=='S': moveable[a]+=1
        member[a]+=1
    for _ in range(c):
        a,b=map(int,input().split())
        seat[a].append(b)
    for i in range(1,n+1):seat[i].sort()
    for i in range(1,l+1):
        if moveable[i]:
            while moveable[i] and seat[i]:
                count=0
                move=min(member[i],seat[i].pop())
                member[i]-=move
                total+=move
                moveable[i]-=1
            
            
    print(f'Data Set {tt+1}:\n{n-total}')
    
