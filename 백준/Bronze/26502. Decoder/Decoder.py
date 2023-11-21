decode={'y':'a','a':'e','e':'i','i':'o','o':'u','u':'y'}
def parse(x):
    answer=[]
    for c in x:
        if c.lower() in decode:
            if c.isupper():answer.append(decode[c.lower()].upper())
            else:answer.append(decode[c])
        else: answer.append(c)
    return ''.join(answer)

for _ in range(int(input())):
    print(parse(input()))
   