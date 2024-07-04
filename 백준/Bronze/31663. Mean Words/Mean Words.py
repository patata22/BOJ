total=[0]*45
count=[0]*45

for _ in range(int(input())):
    temp= list(map(ord, input()))
    for i in range(len(temp)):
        count[i]+=1
        total[i]+=temp[i]

answer=[]
for i in range(45):
    if not count[i]: break
    answer.append(chr(total[i]//count[i]))

print(''.join(answer))
