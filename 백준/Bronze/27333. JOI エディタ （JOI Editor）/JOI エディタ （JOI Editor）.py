n=int(input())
word=list(input())
for i in range(1,n):
    if word[i-1]==word[i]:
        word[i-1]=word[i-1].upper()
        word[i]=word[i].upper()
print(''.join(word))
