def sol():
    stack=[]
    target=1
    for x in number:
        if x==target:
            target+=1
        else:
            while stack and stack[-1]==target:
                target+=1
                stack.pop()
            if stack and stack[-1]<x: return 'Sad'
            else: stack.append(x)
    return 'Nice'

n=int(input())
number=list(map(int,input().split()))
print(sol())