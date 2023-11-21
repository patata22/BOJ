weight=[0]*15
weight[0]=1
for i in range(1,15):
    weight[i]=3*weight[i-1]

for _ in range(int(input())):
    n=int(input())
    i=14
    while 3**i>n:
        i-=1
    answer=[0]*(i+1)
    while i>=0:
        answer[i]=n//weight[i]
        n%=weight[i]
        i-=1
    print(*answer[::-1])