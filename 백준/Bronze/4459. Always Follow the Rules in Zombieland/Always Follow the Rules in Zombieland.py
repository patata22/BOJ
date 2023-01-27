rule={}
for _ in range(1,int(input())+1):
    rule[_]=input()

for _ in range(int(input())):
    x=int(input())
    if x in rule: print(f'Rule {x}: {rule[x]}')
    else: print(f'Rule {x}: No such rule')
