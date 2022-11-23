l=int(input())
score = [0]+ list(map(int,input().split()))
answer_score= -float('inf')
answer=0
for gap in range(1,l+1):
    temp = 0
    for i in range(gap,l+1,gap):
        temp += score[i]
    if temp>answer_score:
        answer= gap
        answer_score= temp
if answer_score<0: print(0,0)
else: print(answer, answer_score)

