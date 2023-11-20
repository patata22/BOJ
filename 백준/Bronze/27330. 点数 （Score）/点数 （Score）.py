n=int(input())
number=list(map(int,input().split()))
input()
zero=set(map(int,input().split()))
score=0
for x in number:
    score+=x
    if score in zero: score=0
print(score)

