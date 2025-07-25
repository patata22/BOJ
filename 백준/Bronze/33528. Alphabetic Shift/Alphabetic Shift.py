word=list(input())
for i in range(26):
    print(''.join(word))
    for j in range(len(word)):
        if word[j]=='A': word[j]='Z'
        else: word[j]=chr(ord(word[j])-1)