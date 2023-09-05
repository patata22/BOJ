dic={'A':4, 'B':3, 'C':2, 'D':1, 'F':0, '+':0.5}

s=input()
total=0
count=0
for x in s:
    if x.isalpha(): count+=1
    total+=dic[x]
print(total/count)