DIV=1000000007

route=[[0,1,1,0,0,0,0,0],
       [1,0,1,1,0,0,0,0],
       [1,1,0,1,1,0,0,0],
       [0,1,1,0,1,1,0,0],
       [0,0,1,1,0,1,0,1],
       [0,0,0,1,1,0,1,0],
       [0,0,0,0,0,1,0,1],
       [0,0,0,0,1,0,1,0]]

def matrixMul(a,b):
    n=len(a)
    m=len(a[0])
    l=len(b[0])
    result=[[0]*l for i in range(n)]
    for i in range(n):
        for k in range(l):
            total=0
            for j in range(m):
                total+=(a[i][j]*b[j][k])%DIV
            result[i][k]=total%DIV
    return result

def sol(n):
    if n==1: return route
    temp=sol(n//2)
    result=matrixMul(temp,temp)
    if n%2: result=matrixMul(result, route)
    return result
            
print(sol(int(input()))[0][0])

   
