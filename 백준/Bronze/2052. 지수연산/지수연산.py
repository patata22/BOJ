a=1
n=int(input())
for _ in range(n):a*=5
a=str(a)
front=['0','.']
for _ in range(n-len(a)):front.append('0')
front.append(str(a))
print(''.join(front))
             

