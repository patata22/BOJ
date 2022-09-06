fib={0:0, 1:1}
def fibonacci(n):
    if n in fib:
        return fib[n]
    else:
        fib[n]=fibonacci(n-1)+fibonacci(n-2)
        return fib[n]
fibonacci(40)
t=int(input())
for _ in range(t):
    n=int(input())
    if n==0:print(1,0)
    else:print(fibonacci(n-1),fibonacci(n))