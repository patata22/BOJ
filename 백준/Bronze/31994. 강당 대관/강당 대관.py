cnt=0
answer=''
for _ in range(7):
    a,b=input().split()
    if int(b)>cnt:
        cnt=int(b)
        answer=a
print(answer)
