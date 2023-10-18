def sol():
    n=int(input())
    now=n%10
    n//=10
    gap=n%10-now
    while n:
        now=n%10
        n//=10
        if n==0: return '◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!'
        if n%10-now!=gap: return '흥칫뿡!! <(￣ ﹌ ￣)>'
    return '◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!'
print(sol())