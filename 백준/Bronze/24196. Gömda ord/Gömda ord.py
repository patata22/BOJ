x=input()
idx=0
answer=[]
while idx<len(x):
    answer.append(x[idx])
    idx+=ord(x[idx])-64
print(''.join(answer))
