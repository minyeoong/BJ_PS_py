# import sys
# sys.setrecursionlimit(2500)
# def fn(n):
#     if n==0:
#         return (1,0)
#     if n==1:
#         return (0,1)
#     else:
#         return tuple(sum(elem) for elem in zip(fn(n-1), fn(n-2)))
    
# N = int(input())
# for i in range(N):
#     n = int(input())
#     lst = list(fn(n))
#     print(lst[0],end=' ')
#     print(lst[1])

# import sys
# sys.setrecursionlimit(2500)
# def f0n(n):
#     if n==0:
#         return 1
#     if n==1:
#         return 0
#     else:
#         return f0n(n-1)+f0n(n-2)
    
# def f1n(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     else:
#         return f1n(n-1)+f1n(n-2)
    
# N = int(input())
# for _ in range(N):
#     n = int(input())
#     print(f0n(n),end=' ')
#     print(f1n(n))


num =[]
N = int(input())
for _ in range(N):
    n = int(input())
    num.append(n)
one = [0 for _ in range(max(num)+2)]
zero =[0 for _ in range(max(num)+2)]
one[0]=0
one[1]=1
zero[0]=1
zero[1]=0
for i in range(2,max(num)+1):
    one[i]=one[i-1]+one[i-2]
    zero[i]=zero[i-1]+zero[i-2]
for j in range(N):
    print(zero[num[j]],end=' ')
    print(one[num[j]])