x=100-int(input())
p=[25,10,5]
answer=[]
for c in p:
    answer.append(x//c)
    x%=c
answer.append(x)
print(*answer)