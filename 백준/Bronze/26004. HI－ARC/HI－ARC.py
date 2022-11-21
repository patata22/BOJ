n=int(input())
alpha=input()
answer=[0]*5
for i in range(n):
    if alpha[i]=='H': answer[0]+=1
    elif alpha[i]=='I': answer[1]+=1
    elif alpha[i]=='A': answer[2]+=1
    elif alpha[i]=='R': answer[3]+=1
    elif alpha[i]=='C': answer[4]+=1

print(min(answer))
