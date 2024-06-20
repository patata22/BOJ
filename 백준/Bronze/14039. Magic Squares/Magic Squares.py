board=[list(map(int,input().split())) for i in range(4)]
number=set()
for i in range(4):
    number.add(sum(board[i]))
for i in range(4):
    temp=0
    for j in range(4):
        temp+=board[j][i]
    number.add(temp)
print('magic') if len(number)==1 else print('not magic')
