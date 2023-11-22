rune={}
for _ in range(int(input())):
    a,b=input().split()
    rune[b]=a

word=input()
answer=[]
for i in range(0,len(word),4):
    if word[i:i+4] in rune: answer.append(rune[word[i:i+4]])
    else: answer.append('?')
print(''.join(answer))
    
