input()
temp=sorted(list(map(int,input().split())))
total=sum(temp)

answer=0
while temp:
    now=temp.pop()
    total-=now
    answer+=total*now
print(answer)