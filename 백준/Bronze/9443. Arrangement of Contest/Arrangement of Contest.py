answer=[0]*26
for _ in range(int(input())):
    answer[ord(input()[0])-65]=1
a=0
for i in range(26):
    if answer[i]:
        a=i+1
    else: break
print(a)