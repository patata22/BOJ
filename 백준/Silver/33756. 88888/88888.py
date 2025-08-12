import sys
input=sys.stdin.readline

def sol(x):
    if x%8: return 'No'
    x//=8
    result=0
    for y in eight:
        result+=x//y
        x%=y
    if result<=8: return 'Yes'
    else: return 'No'

eight=[int('1'*i) for i in range(1,19)][::-1]

answer=[]
for tt in range(int(input())):
    answer.append(sol(int(input())))
print('\n'.join(answer))
