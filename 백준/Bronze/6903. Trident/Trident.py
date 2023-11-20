t=int(input())
s=int(input())
h=int(input())

answer=[]
l=2*s+3
temp=[' ']*l
for i in range(0,l,s+1): temp[i]='*'
for _ in range(t):
    answer.append(''.join(temp))
answer.append('*'*l)
temp=[' ']*l
temp[s+1]='*'
for _ in range(h):answer.append(''.join(temp).rstrip())

for x in answer:
    print(*x, sep='')
