n=int(input())
word= input()
temp=""
answer=0
for i in range(n):
    if 48<=ord(word[i])<=57:
        temp=temp+word[i]
    else:
        if temp and len(temp)<7:answer+=int(temp)
        temp=""

if temp and len(temp)<7:answer+=int(temp)
print(answer)
    
