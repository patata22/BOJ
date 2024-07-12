def sol():
    cnt=0
    while s:
        now=s.pop()
        if now==')': cnt+=sol()
        elif now=='(': return int(s.pop())*cnt
        else: cnt+=1
    return cnt
s=list(input())
print(sol())
