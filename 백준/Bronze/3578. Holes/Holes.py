n=int(input())

if not n: print(1)
elif n==1: print(0)
else:
    answer=[]
    if n%2: answer.append('4')
    for _ in range(n//2): answer.append('8')
    print(''.join(answer))
