import sys
input=sys.stdin.readline
def parse():
    if board[1]=='.##...##.':return '0'
    elif board[1]=='..####...':return '1'
    elif board[-2]=='#########':return '2'
    elif board[2]=='.......##':return '3'
    elif board[4]=='#########':return '4'
    elif board[1]=='.##......':return '5'
    elif board[2]=='##.......':return '6'
    elif board[2]=='.....##..':return '7'
    elif board[-4]=='##.....##':return '8'
    return '9'

answer=[]
for _ in range(int(input())):
    board=[input().rstrip() for i in range(8)]
    answer.append(parse())
print(''.join(answer))