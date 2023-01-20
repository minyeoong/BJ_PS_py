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
'''
그룹 단어란 단어에 존재하는 모든 문자에 대해서,
각 문자가 연속해서 나타나는 경우만을 말한다
그룹단어인 문자열을 체크하는 문제이다.
난이도: 실버5
sol1)
1. 알파벳 각각 접근하지 않고 문자열 전체에 접근
2.그룹 단어에 위배되는 게 있으면 cnt-=1하고 break(없다면 아무 일도 없음)

 if str[j] in str[j+1:]:
 이 라인이 핵심이었음
 연속되는 알파벳을 체크하면서 j를 키워간다. 연속되는 값이 같으면 상관 없지만 다르다면  if str[j] in str[j+1:]:
 을 통해 str[j+1:]에 해당 알파벳이 있는지 체크한다.
'''
def next_idx_func(i,idx):
    next_idx=str.index(i,idx+1)
    return next_idx

N = int(input())
cnt =N
for _ in range(N):
    flag =False
    str = input()
    str_set = list(set(str))
    for i in str_set:
        if str.count(i)<2:
            pass
        else:
            next_idx =str.index(i)
            for _ in range(str.count(i)-1):
                idx = next_idx
                next_idx = next_idx_func(i,next_idx)
                if next_idx-idx!=1:
                    flag=True
                    break
    if flag==True:
        cnt-=1            
print(cnt)
'''
sol2)
1. 검토할 알파벳 선정
2. 알파벳 하나에 대해 그룹단어에 위배되는지 여부 체크
   
string을 배열로 받는다, 1157와 마찬가지로 set함수를 이용해 검토할 알파벳의 중복이 제외된 문자열을 만든다.
N번 문자열을 받을 것이고 각 문자열에 대해 True이면 그룹단어가 아닌 것이고(cnt-=1) False이면 그룹단어이다.
따라서 flag를 N반복문 맨 처음에 초기화 해 주어야 한다.
for i in str_set: 을 통해 문자열에 포함된 알파벳 각각에 대해 접근한다. 
str.count(i)는 해당 알파벳이 몇 개인지 1개라면 pass 2개이상이면 else문
idx와 next_idx의 차가 1이면 True로 바꿔주는 작업을 할 건데 
str.count(i)-1번 반복해준다. 
next_idx를 추출하는 함수를 만든다. 
매개변수는 알파벳, idx(이전 인덱스)
next_idx=str.index(i,idx+1) 
index함수를 이용한다. index(찾을 문자,시작지점,끝지점)
'''