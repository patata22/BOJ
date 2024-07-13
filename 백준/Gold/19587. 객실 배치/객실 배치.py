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

def sol(x):
    if x==1: return original
    temp = sol(x//2)
    result = matrixMul(temp,temp)
    if x%2: result=matrixMul(result, original)

    return result

original = [[1,1,1], [1,0,1], [1,1,0]]
n=int(input())
if n==1: print(3)
else:
    m=sol(n-1)
    print(sum([sum(m[i]) for i in range(3)])%DIV)
