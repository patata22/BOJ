def solution(id_pw, db):
    answer = ''
    
    DB={}
    for id,pw in db:DB[id]=pw
    id,pw=id_pw
    if id in DB:
        if pw==DB[id]: answer="login"
        else: answer="wrong pw"
    else: answer="fail"
    
    return answer