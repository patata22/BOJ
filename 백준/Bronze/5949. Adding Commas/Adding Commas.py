t = list(input())
answer=[]
count=0
while t:
    answer.append(t.pop())
    count+=1
    if count and not count%3:
        answer.append(',')
if answer[-1]==',': answer.pop(-1)
print(''.join(answer[::-1]))