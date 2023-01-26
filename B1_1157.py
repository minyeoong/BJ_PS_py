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


str = input().upper()
str_set= set(str)
max = 0
for i in str_set:
    if max<str.count(i):
        max = str.count(i)
        max_alpha = i
cnt=0
for i in str_set:    
    if max == str.count(i):
       cnt+=1
if cnt>1:
    print('?')
else:
    print(max_alpha) 
    
'''
문자열에서 가장 많이 포함된 문자를 출력하는 문제
중복일 때는 ?를 출력
난이도: 브1

1.모두 대문자로 바꿔준다.
2. set함수를 이용한다.
3. ?가 출력될 경우를 처리해준다.



'''