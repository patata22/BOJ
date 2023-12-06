def change(x,y):
    if x==' ': return x
    return chr((ord(x)-97 - ord(y)+96)%26+97)

a=input()
b=input()
answer=[]
for i in range(len(a)):
    answer.append(change(a[i], b[i%len(b)]))
print(''.join(answer))

