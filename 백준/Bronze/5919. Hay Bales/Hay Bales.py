n=int(input())
number=[int(input()) for i in range(n)]
avg=sum(number)//n
print(sum(map(lambda x: abs(x-avg),number))//2)
