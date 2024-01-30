
def check(a,b,c):
    return int(1<=a<=12 and 0<=b<=59 and 0<=c<=59)

a,b,c=map(int,input().split(':'))
answer=0
answer+=check(a,b,c)
answer+=check(a,c,b)
answer+=check(b,a,c)
answer+=check(b,c,a)
answer+=check(c,a,b)
answer+=check(c,b,a)
print(answer)
          
