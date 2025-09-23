import sys
input=sys.stdin.readline

DIV=10**9+7

def matrixMul(a,b):
    result=[[0]*2 for i in range(2)]
    for i in range(2):
        for j in range(2):
            temp=0
            for k in range(2):
                temp+=a[i][k]*b[k][j]
            result[i][j]=temp%DIV
    return result

def sol(x):
    if x==1: return base
    else:
        temp=sol(x//2)
        result=matrixMul(temp,temp)
        if x%2: result=matrixMul(result,base)
    return result
    

base=[[1,1],[1,0]]
n=int(input())
if n%2:n+=1
print(sol(n)[1][0])
