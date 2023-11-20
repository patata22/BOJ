n=int(input())
answer=[]
word=input().split()
answer.append(word[0][0])
for i in range(1,n):
    if len(word[i-1])>len(word[i]):answer.append(' ')
    else: answer.append(word[i][len(word[i-1])-1])
print(''.join(answer))
