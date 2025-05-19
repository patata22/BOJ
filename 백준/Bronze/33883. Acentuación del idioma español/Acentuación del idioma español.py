word=list(input())
idx=[]
for i in range(len(word)):
    if word[i] in 'aeiou': idx.append(i+1)

if not idx: print(-1)
elif word[-1] in 'aeiouns':
    if len(idx)==1: print(-1)
    else: print(idx[-2])
else: print(idx[-1])
        
