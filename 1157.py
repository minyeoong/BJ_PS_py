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


