a=int(input())
b=int(input())
answer=0
for i in range(1,a+1):
    for j in range(1,b+1):
        if i+j==10: answer+=1
if answer==1: print('There is 1 way to get the sum 10.')
else: print(f'There are {answer} ways to get the sum 10.')
               
