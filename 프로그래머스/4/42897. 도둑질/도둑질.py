def solution(money):
    answer = 0
    n=len(money)
    dp1=[[0]*2 for i in range(n)] 
    dp2=[[0]*2 for i in range(n)]
    dp2[0][1]=money[0]
    for i in range(1,n):
        dp1[i][0]= max(dp1[i-1])
        dp1[i][1]= dp1[i-1][0]+money[i]
    for i in range(1,n-1):
        dp2[i][0]=max(dp2[i-1])
        dp2[i][1]=dp2[i-1][0]+money[i]
    answer=max(max(dp1[-1]), max(dp2[-2]))
    return answer