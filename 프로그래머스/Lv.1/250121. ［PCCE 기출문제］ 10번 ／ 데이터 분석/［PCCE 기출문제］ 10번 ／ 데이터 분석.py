def solution(data, ext, val_ext, sort_by):
    answer = []
    temp=('code', 'date', 'maximum', 'remain')
    ext=temp.index(ext)
    s=temp.index(sort_by)
    
    for d in data:
        if d[ext]<val_ext:
            answer.append(d)
    answer.sort(key=lambda x: x[s])
    
    return answer