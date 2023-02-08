str = list(input())
cnt_one=0
cnt_zero=0
store=str[0]
for i in str:
    if store!=i:
        if store=='0':
            cnt_zero+=1
        if store =='1':
            cnt_one +=1
    store =i
if str[len(str)-1]=='0':
    cnt_zero+=1
else:
    cnt_one+=1
print(min(cnt_one,cnt_zero))

# for i in range(len(str)-1):
#     if str[i]!=str[i+1]:
#         #이와 같은 방법이 더 간단했다.