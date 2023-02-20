N = int(input())
A=[]
B=[]
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse =True)

sum = 0
for i in range(N):
    sum += A[i]*B[i]
    
print(sum)

'''
x+y = k일 때
x*y의 최솟값은 x와 y의 값의 차이가 가장 클 때이다.

'''