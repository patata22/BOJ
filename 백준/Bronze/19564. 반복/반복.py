s=input()
answer=1
now=0
for x in s:
    if ord(x)<=now:
        answer+=1
    now=ord(x)
print(answer)
