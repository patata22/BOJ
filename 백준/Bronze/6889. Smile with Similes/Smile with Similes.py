a=int(input())
b=int(input())
A=[input() for i in range(a)]
B=[input() for i in range(b)]

for i in range(a):
    for j in range(b):
        print(f'{A[i]} as {B[j]}')
