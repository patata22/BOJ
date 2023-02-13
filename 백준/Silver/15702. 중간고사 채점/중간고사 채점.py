n,m=map(int,input().split())

score = tuple(map(int,input().split()))

maxscore=-1
user=0
for i in range(1,m+1):

    temp = input().split()
    number=int(temp[0])
    temp=temp[1:]
    tempscore=0
    for j in range(n):
        if temp[j]=='O':
            tempscore+=score[j]
    if tempscore>maxscore:
        maxscore=tempscore
        user=number
    elif tempscore==maxscore:
        user=min(user,number)

print(user,maxscore)