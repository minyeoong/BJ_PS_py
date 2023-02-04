# T= int(input())
# for _ in range(T):
#     N,M = map(int, input().split())
#     store_M =M
#     N_divisior=[]
#     M_divisior=[]
#     i=2
#     while(N>1):
#         while(N%i==0):
#             N_divisior.append(i)
#             N=N//i
        
#         i+=1
#     i=2
#     while(M>1):
#         while(M%i==0):
#             M_divisior.append(i)
#             M=M//i
#         i+=1
#     result=1
#     for j in N_divisior:
#         if(store_M%j==0):
#             store_M =store_M//j
#         result*=j 
    
#     result*=store_M
#     print(result)
N = int(input())
for _ in range(N):
    n,m =map(int,input().split())
    nstore=n
    mstore =m
    n_div=[]
    m_div=[]
    i =2
    while(1):
        if (n%i ==0):
            n_div.append(i)
            n=n/i
        else:
            i+=1
        if n==1:
            break
    i =2
    while(1):
        if (m%i ==0):
            m_div.append(i)
            m=m/i
        else:
            i+=1
        if m==1:
            break

    # print(n_div)
    # print(m_div)

    for i in n_div:
        if mstore%i ==0:
            mstore=mstore/i
    res = nstore*mstore
    print(int(res))
    


#math 라이브러리 이용
import math

def LCM(a, b):
    return a * b // math.gcd(a, b)

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(LCM(a, b))

'''
난이도: 브1

최소공배수는 두 수를 곱하고 최대공약수로 나누면 된다는 것을 이용하면 된다. 
우선 약수들을 모두 구해 리스트에 각각 넣고 리스트에서 공통적으로 겹치는 약수들을 곱한 수에 
나눠주는 방식을 이용한다.

'''

