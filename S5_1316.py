cnt = int(input())
for _ in range(cnt):
    str = input() #abbbca
    str_set = list(set(str)) #abc
    flag = True
    for i in str_set: #a,b,c
        index = str.index(i)
        for j in range(len(str)): #aabbbca 5번 0,1,2,3,4,5
            if str[j]== i:
                if j-index>1:
                    flag =False
                    break
                else:
                    index = j
    if flag ==False:
        cnt-=1
print(cnt)