top=list(map(int,input().split()))[1:]
answer=0
for _ in range(int(input())):
    eat=1
    for x in list(map(int,input().split()))[1:]:
        if x in top: eat=0
    answer+=eat
print(answer)
        
        
