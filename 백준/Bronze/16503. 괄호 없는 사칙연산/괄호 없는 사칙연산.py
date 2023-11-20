x=input().split()
a=int(eval(''.join(x[:3])))
b=int(eval(''.join(x[2:])))
A=int(eval(str(a)+''.join(x[3:])))
B=int(eval(''.join(x[:2])+str(b)))
print(min(A,B))
print(max(A,B))
      