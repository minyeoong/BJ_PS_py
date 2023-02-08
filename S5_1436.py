end_num = []
for i in range(666,1066700):#그냥 충분히 큰 수 이다.
    #범위를 모르니 그냥 while 문을 쓰는 편이 나았다.
    if "666" in str(i):
        end_num.append(i)

print(end_num[int(input())-1])

#브루트포스 문제이다.

