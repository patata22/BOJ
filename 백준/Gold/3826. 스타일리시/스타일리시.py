#3826

def countIndent(line):
    result=0
    for x in line:
        if x!='.':return result
        result+=1

def count(line):
    r,c,s=0,0,0
    for x in line:
        if x=='(': r+=1
        elif x==')': r-=1
        elif x=='{': c+=1
        elif x=='}': c-=1
        elif x=='[': s+=1
        elif x==']': s-=1
    return r,c,s

def sol(line):
    result=set()
    for i,j,k in cand:
        result.add(r*i+c*j+s*k)
    if len(result)>1: return -1
    return list(result).pop()

while True:
    n,m=map(int,input().split())
    if not n: break
    stylish=[list(input()) for i in range(n)]
    r,c,s = 0,0,0
    cand=set()
    for i in range(1,21):
        for j in range(1,21):
            for k in range(1,21):
                cand.add((i,j,k))

    for line in stylish:
        indent=countIndent(line)
        nxtCand=set()
        for i,j,k in cand:
            if r*i+c*j+s*k==indent: nxtCand.add((i,j,k))
        nr,nc,ns = count(line)
        r+=nr
        c+=nc
        s+=ns
        cand=nxtCand

    unstylish=[list(input()) for i in range(m)]
    r,c,s=0,0,0
    answer=[]
    for line in unstylish:
        answer.append(sol(line))
        nr,nc,ns=count(line)
        r+=nr
        c+=nc
        s+=ns

    print(*answer)
