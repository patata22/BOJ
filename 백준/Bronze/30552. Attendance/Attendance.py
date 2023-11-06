answer=[]
for _ in range(int(input())):
    x=input()
    if x=='Present!':answer.pop()
    else:answer.append(x)
if not answer:print('No Absences')
else:
    for x in answer:print(x)
