x,y = map(int, input().split())
month=[0,31,28,31,30,31,30,31,31,30,31,30]
for i in range(x):
    y+=month[i]
week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
print(week[y%7])
