j,r=map(int,input().split())
number=list(map(int,input().split()))
score=[0]*j
for i in range(j*r):
    score[i%j]+=number[i]
answer=-1
a=0
for i in range(j):
    if score[i]>=answer:
        answer=score[i]
        a=i+1
print(a)