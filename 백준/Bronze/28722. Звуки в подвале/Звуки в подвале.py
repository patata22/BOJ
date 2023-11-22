x=input()
now=x[0]
total=0
for i in range(1,len(x)):
    if x[i]!=now:
        total+=1
    now=x[i]
print('Win') if total%2 else print('Lose')
