n,m=map(int,input().split())
answer=0
number=list(map(lambda x: int(x)-1, input().split()))
board=[list(map(int,input().split())) for i in range(n)]
now=number[0]
for to in number[1:]:
    answer+=board[now][to]
    now=to
print(answer)
