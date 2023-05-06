def factorial(n):
    if n==1: return 1
    if n not in dic:
        dic[n]=n*factorial(n-1)
    return dic[n]
        

dic={}
n=int(input())

print(factorial(2*n)//(factorial(n)*factorial(n)), n*n)
