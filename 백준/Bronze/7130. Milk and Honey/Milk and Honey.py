m,h=map(int,input().split())
answer=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    answer+=max(a*m,b*h)
print(answer)
