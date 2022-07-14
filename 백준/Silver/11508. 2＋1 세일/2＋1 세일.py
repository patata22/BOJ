n=int(input())
price=[int(input()) for i in range(n)]
price.sort(reverse=True)
answer=0
for i in range(0,n,3):
    answer+=price[i]
for i in range(1,n,3):
    answer+=price[i]
print(answer)
