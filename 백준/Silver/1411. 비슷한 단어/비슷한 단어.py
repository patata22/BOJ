def compare(a,b):
    if len(a)!=len(b): return 0
    record={}
    for i in range(len(a)):
        if a[i] not in record:
            record[a[i]]=b[i]
        else:
            if record[a[i]]!=b[i]: return 0
    record={}
    for i in range(len(a)):
        if b[i] not in record:
            record[b[i]]=a[i]
        else:
            if record[b[i]]!=a[i]: return 0
    return 1

n=int(input())
answer=0
word=[input() for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        answer+=compare(word[i],word[j])
print(answer)
