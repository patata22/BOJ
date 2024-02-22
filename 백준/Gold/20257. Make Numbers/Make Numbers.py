def sol(depth):
    if depth==4:
        if len(record)==4: return
        num=eval(''.join(record))
        if num>=0: answer.add(num)
        return
    for i in range(4):
        if not used[i]:
            record.append(number[i])
            used[i]=1
            sol(depth+1)
            if depth!=3:
                for op in oper:
                    record.append(op)
                    sol(depth+1)
                    record.pop()
            used[i]=0
            record.pop()

number=input().split()
oper='+-*'
used=[0]*4
record=[]
answer=set()

sol(0)
print(len(answer))
