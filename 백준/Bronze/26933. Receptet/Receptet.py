answer=0
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if b>a: answer+=(b-a)*c
print(answer)
