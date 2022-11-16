#14550


while True:
    x = input()
    if x== '0': break
    n,s,t = map(int,x.split())
    answer=-float('inf')
    board= [0]
    while len(board)<=n:
        board.extend(map(int,input().split()))
    dp = [[-float('inf')]*(n+1) for i in range(t)]
    for i in range(1,min(n+1,s+1)):
        dp[1][i]=board[i]
    for T in range(2,t):
        for i in range(1,n+1):
            for j in range(1,s+1):
                if i<j: break
                dp[T][i]=max(dp[T][i], dp[T-1][i-j]+board[i])
        
    for i in range(min(n,s),0,-1):
        answer=max(answer, dp[-1][-i])
    print(answer)
