def sol(hp,food):
    answer=0
    while hp!=1:
        answer+=1
        hp//=2
    return answer+food+1

n=int(input())

for _ in range(n):
    a,b=map(int,input().split())
    print(sol(a,b))
    
