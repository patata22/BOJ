n=int(input())
number=[int(input()) for i in range(n)]
one=number[0]
number.sort()
if number[0]==one: print('ez')
elif number[-1]==one: print('hard')
else: print('?')