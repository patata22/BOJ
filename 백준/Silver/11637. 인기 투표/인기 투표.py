for _ in range(int(input())):
    n=int(input())
    total=0
    maxvote=0
    winner=0
    tie=False
    for i in range(1,n+1):
        v=int(input())
        total+=v
        if v>maxvote:
            winner=i
            maxvote=v
            tie=False
        elif v==maxvote:
            tie=True
    if tie: print('no winner')
    else:
        if maxvote*2>total: print(f'majority winner {winner}')
        else: print(f'minority winner {winner}')
        
