lst=[]
year=[]
for _ in range(3):
    a,b,c=input().split()
    lst.append((int(a), c))
    year.append(int(b)%100)

year.sort()
lst.sort(key=lambda x: -x[0])

print(''.join(map(str,year)))
print(lst[0][1][0]+lst[1][1][0]+lst[2][1][0])
