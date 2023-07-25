input()
y=int(input())
answer=0
for x in map(int,input().split()):
    if x**y>0: answer+=x**y
print(answer)
