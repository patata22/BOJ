k=int(input())
n=map(int,input().split())
a=tuple(map(int,input().split()))
m=map(int,input().split())
b=tuple(map(int,input().split()))
answer=0
for x in a:
    for y in b:
        if x+k==y: answer+=1

print(answer)
