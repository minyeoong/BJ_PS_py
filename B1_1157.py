word = input()
WORD=word.upper() #여기서 실수를 했었다 . word.upper()이라고만 했다.
max = 0
for i in set(WORD):
    if(max<WORD.count(i)):
        max = WORD.count(i)
        char = i
cnt=0
for i in set(WORD):
    if(max==WORD.count(i)):
        cnt+=1
if(cnt>1):
    print('?')
elif(cnt==1):
    print(char)

 
# str = input().upper()  #요렇게 input받을 때 upper로 바꿔주면 깔끔
# uniqueStr = list(set(str))
# count_list =[]
# for i in uniqueStr:
#     cnt = str.count(i)
#     count_list.append(cnt)

# if count_list.count(max(count_list))>1:
#     print('?')
# else:
#     special_idx=count_list.index(max(count_list))
#     print(uniqueStr[special_idx])


