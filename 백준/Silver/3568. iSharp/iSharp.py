temp=input().split()

for x in temp[1:]:
    head=temp[0]
    body=list(x)
    body.pop()
    while body:
        if body[-1].isalpha():break
        elif body[-1]==']':
            head+='[]'
            body.pop()
            body.pop()
        else:head+=body.pop()
    body.append(';')
    print(head, ''.join(body))