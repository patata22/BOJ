r={'J':0,'O':1,'I':2}
input()
temp=list(input())
temp.sort(key=lambda x: r[x])
print(''.join(temp))
