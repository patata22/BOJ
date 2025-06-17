n=set([i*i for i in range(1,32625)])
for _ in range(int(input())): print(int(int(input()) in n))