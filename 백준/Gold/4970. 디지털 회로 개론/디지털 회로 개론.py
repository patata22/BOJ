def NOT(x):
    return 2-x

def AND(x,y):
    return min(x,y)

def OR(x,y):
    return max(x,y)

def parse():
    while stack:
        now = stack.pop()
        if now == ')':temp.append(parse())
        elif now in value:temp.append(value[now])
        elif now=='-':temp.append(NOT(temp.pop()))
        elif now=='*':flag=1
        elif now=='+':flag=0
        elif now=='(':
            if flag:return AND(temp.pop(),temp.pop())
            else:return OR(temp.pop(),temp.pop())
        else: temp.append(int(now))
    return temp.pop()

value={'P': -1, 'Q': -1, 'R': -1}
answer=0
while True:
    DATA=list(input().rstrip())
    if DATA==['.']: break
    answer=0
    temp=[]
    for _ in range(3):
        value['P']=_
        for __ in range(3):
            value['Q']=__
            for ___ in range(3):
                value['R']=___
                stack = DATA[:]
                if parse()==2:answer+=1
    print(answer)
