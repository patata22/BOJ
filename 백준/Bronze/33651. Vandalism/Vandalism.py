x=input()
answer=[]
for y in 'UAPC':
    if y not in x: answer.append(y)
print(''.join(answer))
