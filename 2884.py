# H, M = map(int,input().split())
# time = H*60+M
# time -=45
# if time< 0:
#     time+=1440
# print(int(time/60),end=' ')
# print(time%60)


h, m = map(int, input().split())
h, m = (h * 60 + m - 45) % 1440 // 60, (h * 60 + m - 45) % 60
print(h, m)
