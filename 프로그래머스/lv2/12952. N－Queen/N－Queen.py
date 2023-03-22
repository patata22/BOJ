def solution(n):
    answer = 0
    col=[0]*n
    rd=[0]*(2*n)
    ld=[0]*(2*n)
    def queen(x):
        nonlocal answer
        if x==n:
            answer+=1
            return
        for y in range(n):
            if not col[y] and not ld[x+y] and not rd[x-y+n-1]:
                col[y]=1
                ld[x+y]=1
                rd[x-y+n-1]=1
                queen(x+1)
                col[y]=0
                ld[x+y]=0
                rd[x-y+n-1]=0
    queen(0)
    return answer
