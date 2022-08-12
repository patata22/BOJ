answer=set()

for _ in range(int(input())):
    count=[0]*26
    word=input()
    for x in word:
        count[ord(x)-97]+=1
    answer.add(''.join(map(str,count)))
print(len(answer))
    
