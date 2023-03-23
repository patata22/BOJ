def solution(line):
    answer=[]
    
    n=len(line)
    top,right=-float('inf'), -float('inf')
    left,bottom = float('inf'), float('inf')
    point=[]
    
    for i in range(n):
        a,b,e = line[i]
        for j in range(i+1,n):
            c,d,f = line[j]
            if not a*d-b*c: continue
            crossX, crossY = (1/(a*d-b*c))*(b*f-e*d), (1/(a*d-b*c))*(e*c-a*f)
            if not (b*f-e*d)%(a*d-b*c) and not (e*c-a*f)%(a*d-b*c):
                crossX, crossY = (b*f-e*d)//(a*d-b*c), (e*c-a*f)//(a*d-b*c)
#            if crossX==int(crossX) and crossY==int(crossY):
 #               crossX,crossY=int(crossX),int(crossY)
                point.append((crossX,crossY))
                top,bottom = max(top, crossY), min(bottom, crossY)
                left,right=min(left, crossX), max(right, crossX)

    
    n=top-bottom+1
    m=right-left+1
    board=[["."]*m for i in range(n)]
    for x,y in point:
        board[y-bottom][x-left]='*'
    for i in range(n):
        answer.append(''.join(board[i]))
    return answer[::-1]