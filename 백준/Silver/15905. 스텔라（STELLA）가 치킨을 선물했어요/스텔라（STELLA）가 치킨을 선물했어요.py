score= [tuple(map(int,input().split())) for i in range(int(input()))]
score.sort(key=lambda x: (-x[0],x[1]))

answer=0
five = score[4][0]
for i in range(5,len(score)):
    if score[i][0]==five:
        answer+=1
    else: break
print(answer)
