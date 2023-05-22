n=int(input())-1
word="baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan".split()
a,b=divmod(n,14)
if word[b] in ('tururu', 'turu'):
    temp= word[b]+'ru'*a
    if len(temp)<=10: print(temp)
    else:
        print('tu+ru*',(len(temp)-2)//2, sep='')
    
else:print(word[b])
