a,b=map(int,input().split(':'))
c,d=map(int,input().split(':'))
answer='NO'
for i in range(c,10):
    for j in range(d,10):
        if a==i and b==j: answer='YES'
print(answer)