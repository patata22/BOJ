import sys
input=sys.stdin.readline

n,m=map(int,input().split())
for _ in range(m):
    pos=[]
    neg=[]
    zero=0
    for x in map(int,input().split()):
        if x>0: pos.append(x)
        elif not x: zero=1
        else: neg.append(x)
    pos.sort()
    neg.sort(reverse=True)
    if not pos:
        if len(neg)<2:
            if zero: print(0)
            else: print(neg.pop())
        else:
            answer=1
            while len(neg)>1:
                answer*=neg.pop()
                answer*=neg.pop()
            print(answer)
    else:
        answer=1
        while pos: answer*=pos.pop()
        while len(neg)>1:
            answer*=neg.pop()
            answer*=neg.pop()
        print(answer)
