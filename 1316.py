# N = int(input())
# cnt = N
# for i in range(N):
#     str = input()
#     for j in range(len(str)-1):
#         if str[j]==str[j+1]:
#             pass
#         else:
#             if str[j] in str[j+1:]: #str[j+1:]가 또 하나의 문자열임
#                 cnt-=1
#                 break
# print(cnt)
'''
그룹 단어란 단어에 존재하는 모든 문자에 대해서,
각 문자가 연속해서 나타나는 경우만을 말한다
그룹단어인 문자열을 체크하는 문제이다.
난이도: 실버5
            
            
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