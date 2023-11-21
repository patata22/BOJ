word=input()
n=len(word)
answer=[]
for i in range(1,n):
    if word[:i]==word[:i][::-1] and word[i:]==word[i:][::-1]:
        answer=[word[:i],word[i:]]
        break
if answer:print(*answer)
else: print("NO")
    
