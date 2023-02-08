str = list(input())
str.sort(reverse =True)
for i in str:
    print(i,end='')
    
#print(''.join(str))


#한 줄 컷도 가능하다 ㅋㅋㅋ
print(''.join(sorted(input(), reverse=True)))
