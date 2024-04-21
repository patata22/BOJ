DIV=10**9+7

def matrixMul(a,b):
    n=len(a)
    m=len(a[0])
    o=len(b[0])
    result=[[0]*o for i in range(n)]
    for i in range(n):
        for j in range(o):
            for k in range(m):
                result[i][j]+=a[i][k]*b[k][j]
            result[i][j]%=DIV
    return result
            
def sol(n):
    if n==1:
        return original
    temp=sol(n//2)
    result=matrixMul(temp,temp)
    if n%2: result=matrixMul(result,original)
    return result

original = [[1,1],[1,0]]
n=int(input())
print(sol(n)[0][1])