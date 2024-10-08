answer=0
now=0
word=list(map(lambda x: ord(x)-65, input()))
for x in word:
    answer+=min((x-now)%26,(now+26-x)%26)
    now=x
print(answer)
