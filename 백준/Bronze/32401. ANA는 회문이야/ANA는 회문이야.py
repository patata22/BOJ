def find(i):
    level=0
    for j in range(i+1,n):
        if level==0 and word[j]=='N':
            level=1
        elif level==0 and word[j]=='A':
            return 0
        elif level==1 and word[j]=='N':
            return 0
        elif level==1 and word[j]=='A':
            return 1
    return 0

n=int(input())
word=list(input())
answer=0
for i in range(n-2):
    if word[i]=='A':
        answer+=find(i)
print(answer)

