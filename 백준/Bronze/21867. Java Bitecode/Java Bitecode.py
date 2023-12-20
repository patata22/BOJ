def parse(x):
    jav='JAVjav'
    if x in jav: return ''
    return x

input()
answer=''.join(map(lambda x: parse(x),input()))
if not answer:print('nojava')
else:print(answer)