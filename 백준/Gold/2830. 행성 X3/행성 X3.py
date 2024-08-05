import sys
input=sys.stdin.readline

n=int(input())
zero=[0]*20
one=[0]*20

for _ in range(n):
    x=int(input())
    for __ in range(20):
        if x%2: one[__]+=1
        else: zero[__]+=1
        x//=2


answer=0
for _ in range(20):
    answer+=(one[_]*zero[_])<<_

print(answer)
