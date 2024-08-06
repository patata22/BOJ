def change(x):
    answer=[]
    for _ in range(6):
        answer.append(str(x%2))
        x//=2
    return answer[::-1]
    
for tt in range(int(input())):
    t=list(map(lambda x: change(int(x)),input().split(':')))
    answer1=[]
    for j in range(6):
        for i in range(3):
            answer1.append(t[i][j])
    answer2=[]
    for x in t: answer2.append(''.join(x))
    
    print(''.join(answer1),''.join(answer2))
