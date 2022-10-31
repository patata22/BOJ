word = input()
cand = []
l = len(word)
for i in range(1,l-1):
    for j in range(i+1,l):
        a=word[0:i]
        b=word[i:j]
        c=word[j:]
        cand.append(a[::-1]+b[::-1]+c[::-1])
cand.sort()
print(cand[0])
