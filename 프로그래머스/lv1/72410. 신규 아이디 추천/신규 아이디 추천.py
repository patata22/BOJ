def solution(new_id):
    return longer(shorter(isNone(removedots(removeSpecial(new_id.lower())))))

def removeSpecial(id):
    temp=""
    for x in id:
        if x.isalpha() or x.isdigit() or x in ('-', '_','.'):
            temp+=x
    return temp

def removedots(id):
    temp=""
    for x in id.strip('.'):
        if x=='.' and temp[-1]=='.': continue
        else:temp+=x
    return temp

def isNone(id):
    if not id: return 'a'
    else: return id

def shorter(id):
    return id[:15].rstrip('.')

def longer(id):
    temp=id
    while len(temp)<3:
        temp+=temp[-1]
    return temp

