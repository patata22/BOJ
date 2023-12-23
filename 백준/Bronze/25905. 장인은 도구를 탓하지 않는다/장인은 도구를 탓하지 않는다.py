hammer=[float(input())*10 for i in range(10)]
hammer.sort(reverse=True)
hammer.pop()
head=1
for x in hammer: head*=x
for i in range(2,10):
    head/=i
print(head)
