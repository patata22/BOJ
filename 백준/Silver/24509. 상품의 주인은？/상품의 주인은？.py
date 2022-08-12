import sys
input=sys.stdin.readline

n=int(input())
score=[list(map(int,input().split())) for i in range(n)]
prize=[]

for j in range(1,5):
    max_score=-1
    winner=-1
    for i in range(n):
        if score[i][0] in prize:continue
        if score[i][j]>max_score or (score[i][j]==max_score and score[i][0]<winner):
            max_score=score[i][j]
            winner=score[i][0]
    
    prize.append(winner)
for x in prize: print(x, end=' ')
            
