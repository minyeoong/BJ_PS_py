# def A(n):
#     sum=0
#     i =1
#     length=0
#     while(sum<n):
#         sum+=i
#         i+=1
#     return i-1 #마지막에 i를 한번 더 더해주니까 i를 1빼준 것을 return 한다.

# n,m =map(int,input().split())
# total=0
# for i in range(n,m+1):
#     total+=A(i)
# print(total)

#아래의 코드는 직접 수열을 다 만들어 놓은 후 진행하는 것이다. 

# a,b=map(int,input().split())
# data=[0]
# sum=0

# for i in range(1,b+1):
#   for j in range(i):
#     data.append(i)

# for i in range(a, b+1):
#   sum+=data[i]
# print(sum)

n,m =map(int,input().split())
series =[]
for i in range(1,50): #range(1,m+1) 이 가장 효율적일 것이다.
    for _ in range(i):
        series.append(i)
print(series)
sum =0
for i in range(n-1,m):
    sum+=series[i]
print(sum)

'''
난이도: 브1

이중포문을 통해 배열을 초기화한다. 
'''