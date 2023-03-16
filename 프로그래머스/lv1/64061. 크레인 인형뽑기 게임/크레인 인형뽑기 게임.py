def solution(board, moves):
    answer = 0
    n=len(board)
    m=len(board[0])
    stack=[]
    for move in moves:
        move-=1
        catched=False
        for i in range(n):
            if board[i][move]:
                catch=board[i][move]
                board[i][move]=0
                catched=True
                break
        if catched:
            if stack and stack[-1]==catch:
                answer+=2
                stack.pop()
            else:stack.append(catch)
        
    
    return answer