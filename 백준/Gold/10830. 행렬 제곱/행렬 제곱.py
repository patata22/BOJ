DIV=1000

def matrixMul(a,b):
    result=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            temp=0
            for k in range(n):
                temp+=a[i][k]*b[k][j]
            result[i][j]=temp%DIV
    return result

def sol(n):
    if n==1: return original
    temp=sol(n//2)
    result = matrixMul(temp,temp)
    if n%2: result=matrixMul(result,original)
    return result
    
n,b=map(int,input().split())
original=[list(map(lambda x: int(x)%1000,input().split())) for i in range(n)]
answer=sol(b)
for i in range(n): print(*answer[i])