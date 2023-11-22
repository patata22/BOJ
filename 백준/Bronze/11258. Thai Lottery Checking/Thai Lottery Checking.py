win,prize=input().split()
prize=int(prize)
head={}
for _ in range(2):
    a,b=input().split()
    head[a]=int(b)
tail={}
for _ in range(3):
    a,b=input().split()
    tail[a]=int(b)

while True:
    x=input()
    if x=='-1': break
    answer=0
    if x==win: answer+=prize
    if x[:3] in head: answer+=head[x[:3]]
    if x[3:] in tail: answer+=tail[x[3:]]
    if x[4:] in tail: answer+=tail[x[4:]]
    print(answer)