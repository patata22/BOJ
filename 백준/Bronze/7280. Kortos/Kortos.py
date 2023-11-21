card=set()
for i in ('B','K','V','S'):
    for j in range(1,14):
        card.add((i,j))
for _ in range(51):
    a,b=input().split()
    card.remove((a,int(b)))
for x,y in card:print(x,y)