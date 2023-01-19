str = input().upper()
uniqueStr = list(set(str))
count_list =[]
for i in uniqueStr:
    cnt = str.count(i)
    count_list.append(cnt)

if count_list.count(max(count_list))>1:
    print('?')
else:
    special_idx=count_list.index(max(count_list))
    print(uniqueStr[special_idx])

'''
문자열을 받았을 때 대소문자 구분 없이 가장 빈도수가 높은 알파벳을 대문자로 출력
난이도 : 브론즈1
1. 대문자, 소문자 구분
2. 빈도수가 높은 알파벳이 여러 개일 때 '?'을 출력

string으로 input을 받을 때 upper()을 통해 모두 대문자로 만들어 준다.
uniqueStr에서 set함수를 이용하여 str 이 갖고 있는 알파벳을 집합으로(중복을 없앤다.)
uniqueStr의 모든 문자 값에 대하여 반복문을 진행한다.
str.count(i)을 통해 처음 받은 str문자열에 포함된 모든 문자에 대하여 count를 세어 주고
count_list에 그 값을 append한다. 
count_list에는 숫자가 저장 돼 있는데 max숫자가 중복이 될 수 있으므로 
count_list.count(max(count_list))>1 이면 ?를 출력한다.
maxr값이 중복이 아니라면 index(max(count_list))를 통해 
uniqueStr에서 max문자를 갖는 index를 추출한다.
'''

