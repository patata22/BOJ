DIV=1000000009

answer=0
x=input()
if x[0]=='c':answer=26
else: answer=10

for i in range(1,len(x)):
    if x[i]=='c':
        if x[i-1]=='c':answer*=25
        else: answer*=26
    else:
        if x[i-1]=='d': answer*=9
        else: answer*=10
    answer%=DIV

print(answer)