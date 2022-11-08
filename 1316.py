N = int(input())
cnt = N
for i in range(N):
    str = input()
    for j in range(len(str)-1):
        if str[j]==str[j+1]:
            pass
        else:
            if str[j] in str[j+1:]: #str[j+1:]가 또 하나의 문자열임
                cnt-=1
                break
print(cnt)
