answer=[i for i in range(101)]

for _ in range(int(input())):
    a,b=input().split()
    b=int(b)
    for i in range(1,101):
        if answer[i]==-1: continue
        if a=='ADD':
            answer[i]+=b
        elif a=='SUBTRACT':
            answer[i]-=b
            if answer[i]<0:
                answer[i]=-1
        elif a=='MULTIPLY':
            answer[i]*=b
        else:
            if answer[i]%b: answer[i]=-1
            else: answer[i]//=b

print(answer.count(-1))