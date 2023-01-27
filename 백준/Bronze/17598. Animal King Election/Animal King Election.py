L=0
T=0
for _ in range(9):
    if input()=='Lion':L+=1
    else:T+=1
print('Lion') if L>T else print('Tiger')