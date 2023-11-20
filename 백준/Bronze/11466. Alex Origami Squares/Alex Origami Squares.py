h,w=map(int,input().split())
if w>h: h,w=w,h
print(max(min(w,h/3), w/2))
