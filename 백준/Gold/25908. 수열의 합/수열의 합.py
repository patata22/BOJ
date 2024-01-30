def sol(x):
    total=0
    for i in range(1,x+1):
        temp=x//i
        if i%2: total-=temp
        else:total+=temp
    return total

s,t=map(int,input().split())
print(sol(t)-sol(s-1))
