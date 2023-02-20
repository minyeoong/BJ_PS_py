N = int(input())
input_num= list(map(int,input().split()))

prime =[False for i in range(260000)]
for j in range(2,500):
    for i in range(2,501):
        prime[j*i]=True
for i in input_num:
    if i ==1 or prime[i]==True:
        N-=1
print(N)

