n=int(input())
five = 0
N=n
while N:
    five+=N//5
    N//= 5
answer = 1
for i in range(1,n+1):
    I=i
    while not I%5:
      I//=5
    if five  and not I%2:
        five-=1
        I//=2
    answer = (answer*I)%10
print(answer)
