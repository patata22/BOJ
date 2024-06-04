ori=['G...', '.I.T','..S.']
n=int(input())
answer=[]

for x in ori:
    temp=[]
    for y in x:
        for _ in range(n):
            temp.append(y)
    for _ in range(n):
        print(''.join(temp))
        
