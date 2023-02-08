# str =[]
# N = int(input())
# for _ in range(N):
#     str.append(input())


# str = list(set(str))
# # for i in range(1,len(str)):
# #     key = len(str[i])
# #     j =i-1
# #     while( j>=0 and len(str[j])>key):
# #         str[j+1]=str[j] 
# #         j -=1
# #     str[j+1]=str[i] #여기가 문제다!!! 
# #     # i=2 일때 hesitate가 but자리로 오므로 
# #     # 자리가 조정된 상황에서 str[i]는 (str[2])는 hesitate이다.
# #     #기준이 되는 key는 변하지 않아야 하는데 그러려면 
# #     #key의 len을 저장하는 것이 아닌 key에 값 자체를 저장했어야 한다. 
# #     #key값 이 원래 저장 돼 있던 index에 다른 값이 올 수 있기 때문이다.
# #     #['wait', 'hesitate', 'but', 'i',..]이런 상황에서 
# #     #i가 2일때 문제가 발생한다
# #     #즉, i가 바뀌진 않지만 str[i]는 바뀌므로 대입하는 값이
# #     # 달라질 수 있다는 것이다. 

# for i in range(1, len(str)):
#         key = str[i] 
#         j = i - 1
#         while j >= 0 and len(str[j]) > len(key):
#             if str[j]>key:
#                 break
#             else:
#                 pass
#             str[j + 1] = str[j]
#             j -= 1
#         str[j + 1] = key
        
# for i in range(len(str)):
#     print(str[i])

N = int(input())
strs = []
for _ in range(N):
    strs.append(input())

    # remove duplicates
strs = list(set(strs))

for i in range(1, len(strs)):
    key = strs[i]
    j = i - 1
    while j >= 0 and (len(strs[j]) > len(key) or (len(strs[j]) == len(key) and strs[j] > key)):
        #길이가 같은 경우엔 사전 순서가 기준이 된다. (len(strs[j]) == len(key) and strs[j] > key) 
        strs[j + 1] = strs[j]
        j -= 1
    strs[j + 1] = key
    
for word in strs:
    print(word)



N = int(input())
strs = []
for _ in range(N):
    strs.append(input())

    # remove duplicates
strs = list(set(strs))

    # sort strings based on length
strs.sort(key=lambda x: (len(x), x))

for word in strs:
    print(word)



n = int(input())
lst = []

for i in range(n):
    lst.append(input())
lst = list(set(lst)) #set을 다시 list로 바꿔 줘야 한다.
#set은 순서가 없기 때문에 순서가 있는 list 나 tuple로 다시 바꿔야 한다.
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)
