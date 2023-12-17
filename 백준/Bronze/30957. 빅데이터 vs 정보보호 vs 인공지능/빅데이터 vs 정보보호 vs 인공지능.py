input()
x=input()
y='BSA'
m=0
for _ in y: m=max(x.count(_),m)
answer=[]
for _ in y:
    if x.count(_)==m:answer.append(_)
if len(answer)==3: print('SCU')
else:print(''.join(answer))
