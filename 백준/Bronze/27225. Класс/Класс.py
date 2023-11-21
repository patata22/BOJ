n,m=int(input()),int(input())
x=min(n,m)
answer=2*min(n,m)
n-=x
m-=x
answer+=n%2+m%2
print(answer)
