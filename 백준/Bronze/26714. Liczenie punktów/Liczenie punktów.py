n=int(input())
N=n//10
test=input()
answer=0
for i in range(0,n,N):
    point=1
    for j in range(i,i+N):
        if test[j]=='N':point=0
    answer+=point
print(answer)