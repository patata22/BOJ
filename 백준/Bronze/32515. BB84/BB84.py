def sol():
    temp=[]
    for i in range(n):
        if keyA[i]==keyB[i]:
            if valueA[i]!=valueB[i]: return 'htg!'
            temp.append(valueA[i])
    return ''.join(temp)

n=int(input())
keyA=list(input())
valueA=list(input())
keyB=list(input())
valueB=list(input())

print(sol())
