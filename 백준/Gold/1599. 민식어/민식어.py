def parse(x):
    n=len(x)
    i=0
    temp=[]
    while i<n:
        if x[i]=='n':
            
            if i+1<n and x[i+1]=='g':
                temp.append(change['ng'])
                i+=1
            else: temp.append(change['n'])
        else: temp.append(change[x[i]])
        i+=1
    return temp
def re(c):
    temp=[]
    for x in c:
        temp.append(reverse[x])
    return ''.join(temp)

origin=['a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'ng', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y']
change={}
reverse={}
for i in range(len(origin)):
    change[origin[i]]=i
    reverse[i]=origin[i]

word=[parse(input()) for i in range(int(input()))]
word.sort()

for x in word:
    print(re(x))
