tt=0
while True:
    tt+=1
    n=int(input())
    if not n: break
    number=list(map(int,input().split()))
    answer=0
    finished=False
    while answer<=1000:
        nxt=[]
        answer+=1
        for i in range(1,n):
            nxt.append(abs(number[i]-number[i-1]))
        nxt.append(abs(number[-1]-number[0]))
        if sum(nxt)==0:
            finished=True
            print(f'Case {tt}: {answer-1} iterations')
            break
        else: number=nxt
    if not finished: print(f'Case {tt}: not attained')