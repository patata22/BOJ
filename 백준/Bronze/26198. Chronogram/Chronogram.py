num={'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
for _ in range(int(input())):
    temp=0
    for x in input():
        if x in num: temp+=num[x]
    print(temp)
