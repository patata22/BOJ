month={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
d,m=map(int,input().split())
total=0
for i in range(1,m):
    total+=month[i]
total+=d
total%=7
answer=['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
print(answer[total])
