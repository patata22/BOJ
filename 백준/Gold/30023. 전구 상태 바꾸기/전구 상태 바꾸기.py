def parse(x):
    if x=='R': return 0
    elif x=='G': return 1
    else:return 2

def red():
    color=word[:]
    answer=0
    for i in range(n-2):
        if color[i]==0: continue
        else:
            if color[i]==1:
                answer+=2
                color[i+1]=(color[i+1]+2)%3
                color[i+2]=(color[i+2]+2)%3
            elif color[i]==2:
                answer+=1
                color[i+1]=(color[i+1]+1)%3
                color[i+2]=(color[i+2]+1)%3
    if color[-1]==color[-2]==0: return answer
    else: return float('inf')

def green():
    color=word[:]
    answer=0
    for i in range(n-2):
        if color[i]==1: continue
        else:
            if color[i]==2:
                answer+=2
                color[i+1]=(color[i+1]+2)%3
                color[i+2]=(color[i+2]+2)%3
            elif color[i]==0:
                answer+=1
                color[i+1]=(color[i+1]+1)%3
                color[i+2]=(color[i+2]+1)%3
    if color[-1]==color[-2]==1: return answer
    else: return float('inf')


def blue():
    color=word[:]
    answer=0
    for i in range(n-2):
        if color[i]==2: continue
        else:
            if color[i]==0:
                answer+=2
                color[i+1]=(color[i+1]+2)%3
                color[i+2]=(color[i+2]+2)%3
            elif color[i]==1:
                answer+=1
                color[i+1]=(color[i+1]+1)%3
                color[i+2]=(color[i+2]+1)%3
    if color[-1]==color[-2]==2: return answer
    else: return float('inf')
                

n=int(input())
word=list(map(parse, input()))
answer=min(red(),blue(),green())
if answer==float('inf'):print(-1)
else: print(answer)


