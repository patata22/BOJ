import sys
input=sys.stdin.readline

for t in range(int(input())):
    if t:print()
    n=int(input())
    game=[]
    answer=0
    day={}
    for _ in range(n):
        a,b,c=map(int,input().split())
        game.append((a,b,c))
    game.sort(key=lambda x: (x[2],x[1]))
    for a,b,c in game:
        if a not in day or day[a]<=b:
            day[a]=c
            answer+=1
    print(f'Scenario #{t+1}:')
    print(answer)
    
    
        
