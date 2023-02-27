n=int(input())
answer=0
a=[input() for i in range(n)]
b=[input() for i in range(n)]
for i in range(n):
    if a[i]==b[i]:answer+=1
print(answer)