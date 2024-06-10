def change(x):
    temp=[]
    while x:
        temp.append(chr((x%26)+97))
        x//=26
    while len(temp)<13: temp.append('a')
    return ''.join(temp[::-1])

def parse(value):
    mul=26**12
    answer=0
    for x in value:
        temp=ord(x)-97
        answer+=mul*temp
        mul//=26
    return answer

if input()=='1':print(change(sum(map(int,input().split()))))
else:print(parse(input()))
