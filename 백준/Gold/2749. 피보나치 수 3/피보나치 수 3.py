DIV=1000000
A=[[1,1],[1,0]]

def matrixMul(a,b):
    result=[[0,0],[0,0]]
    result[0][0]=((a[0][0]*b[0][0])%DIV+(a[0][1]*b[1][0])%DIV)%DIV
    result[0][1]=((a[0][0]*b[0][1])%DIV+(a[0][1]*b[1][1])%DIV)%DIV
    result[1][0]=((a[1][0]*b[0][0])%DIV+(a[1][1]*b[1][0])%DIV)%DIV
    result[1][1]=((a[1][0]*b[0][1])%DIV+(a[1][1]*b[1][1])%DIV)%DIV
    return result

def divide(x):
    if x==1: return A
    temp=divide(x//2)
    result=matrixMul(temp,temp)
    if x%2: result=matrixMul(result,A)
    return result

result=divide(int(input()))
print(result[1][0])
