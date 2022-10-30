answer=0
for _ in range(int(input())):
    a,d,g=map(int,input().split())
    temp = a*(d+g)
    if a==(d+g):temp*=2
    answer=max(temp,answer)
print(answer)
