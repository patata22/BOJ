n,a,b=map(int,input().split())
A=sorted(list(map(int,input().split())))
B=sorted(list(map(int,input().split())))

answer=0
if n%2: answer+=A.pop()
for _ in range(n//2):
    
    if len(A)>1 and B:
        if A[-1]+A[-2]>B[-1]:
            answer+=A.pop()+A.pop()
        else: answer+=B.pop()
    elif not B: answer+=A.pop()+A.pop()
    else: answer+=B.pop()


print(answer)

