white=0
black=0
score={'k':0,'p':1,'n':3,'b':3,'r':5,'q':9}
for _ in range(8):
    temp=input()
    for x in temp:
        if x=='.':continue
        elif x.isupper(): white+=score[x.lower()]
        else: black+=score[x]
        
print(white-black)
