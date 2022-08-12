budget=5*(10**6)

for _ in range(int(input())):
    cost=0
    plan=[]
    while True:
        x=int(input())
        if not x: break
        else: plan.append(int(x))
    plan.sort(reverse = True)
    t=1
    for x in plan:
        cost+=2*(x**t)
        t+=1
    print(cost) if cost<=budget else print("Too expensive")
    

        
        
