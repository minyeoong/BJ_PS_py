# import itertools
# nanjaeng=[]
# for i in range(9):
#     nanjaeng.append(int(input()))
# nC7=list(itertools.combinations(nanjaeng,7))
# print(nC7[0])
# for i in range(len(nC7)):
#     if(sum(nC7[i])==100):
#         nanlist = list(nC7[i])
# nanlist.sort()
# for i in nanlist:
#     print(i)

Nanjang =[]
for _ in range(9):
    h = int(input())
    Nanjang.append(h)
Nanjang.sort()
for i in range(9):
    for j in range(i+1,len(Nanjang)):
        if sum(Nanjang)-Nanjang[i]-Nanjang[j] ==100:
            for k in range(9):
                if k==i or k ==j:
                    pass
                else:
                    print(Nanjang[k])
            exit()

'''
난이도: 브1
9C2 combination을 통해 2개를 빼서 100이되면 출력을 한다.
인덱스로 접근을 하고 조합의 원리에 따라 i , j , k로 알맞게 접근한다.!
'''