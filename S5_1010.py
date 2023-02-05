import sys
sys.setrecursionlimit(10**6)

def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

def nCm(n,m):
    return factorial(n)/(factorial(m)*factorial(n-m))

N = int(input())
for _ in range(N):
    m,n =map(int,input().split())
    print(int(nCm(n,m)))

'''
combination 문제이다. combination함수를 만들기 위해 factorial함수를 먼저 만들었다.
if n==0 상황을 가정하지 않아 문제가 발생했었다.
import sys 
sys.setrecursionlimit()함수를 통해 recursion깊이를 조정할 수 있었다.
'''
