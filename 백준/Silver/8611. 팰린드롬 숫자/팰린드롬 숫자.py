def sol(n,k):
    global nie
    change=""
    while n:
        change+=str(n%k)
        n//=k
    if change==change[::-1]:
        nie=False
        print(k,change)

n=int(input())
nie=True
for i in range(2,11):
    sol(n,i)
if nie:print('NIE')
        