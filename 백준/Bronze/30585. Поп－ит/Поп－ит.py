n,m=map(int,input().split())
one=0
zero=0
for _ in range(n):
    temp=input()
    one+=temp.count('1')
    zero+=temp.count('0')

print(min(n*m-one, n*m-zero))
