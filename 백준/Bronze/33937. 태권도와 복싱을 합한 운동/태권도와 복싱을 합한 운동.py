def parse(X):
    flag=False
    result=[]
    for x in X:
        if x in 'aeiou':
            flag=True
            result.append(x)
        else:
            if flag: return ''.join(result)
            else: result.append(x)
    return ''

A=parse(input())
B=parse(input())
if not A or not B: print('no such exercise')
else: print(A+B)