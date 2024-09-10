import heapq

tt=0
while True:
    temp=input()
    if temp[0]=='0': break
    tt+=1
    print(f'Simulation {tt}')
    size, cmd = temp.split()
    size=int(size)
    inCache=[float('inf')]*26
    memory=[]
    answer=[]
    n=0
    for t in range(len(cmd)):
        x=cmd[t]
        if x=='!':
            temp=[]
            for i in range(26):
                if inCache[i]!=float('inf'):
                    temp.append(chr(i+65))
            answer.append(''.join(sorted(temp, key=lambda x: inCache[ord(x)-65])))
        else:
            o = ord(x)-65
            if inCache[o]==float('inf'):
                if n>=size:
                    tg=min(inCache)
                    for i in range(26):
                        if inCache[i]==tg:
                            inCache[i]=float('inf')
                            break
                else:n+=1    
            inCache[o]=t
    print(*answer, sep='\n')
