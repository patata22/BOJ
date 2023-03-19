def solution(files):
    files.sort(key=lambda x: parse(x))
    return files

def parse(name):
    i=0
    head=""
    number=""
    while not name[i].isdigit():
        head+=name[i]
        i+=1
    for j in range(i,min(i+5, len(name))):
        if not name[j].isdigit(): break
        number+=name[j]
    return head.lower(), int(number)