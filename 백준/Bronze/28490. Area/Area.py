answer=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    answer=max(answer,a*b)

print(answer)