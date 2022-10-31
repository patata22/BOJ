def factorial(x):
    answer=1
    for i in range(1,x+1):
        answer*=i
    return str(answer)

a = factorial(int(input()))

print(a.count('0'))
