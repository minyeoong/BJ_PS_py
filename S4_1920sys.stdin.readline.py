import sys

# Read in the values of n and the list A
n = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))

# Read in the values of m and the list B
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
'''
A의 순서는 중요하지 않지만 B의 순서는 중요하다 
따라서 A는 set을 쓰면서 running time을 향상시킨다. 
set은 순서가 없기 때문에 더 빠른 계산이 가능하다.
'''

# Check if each value in B is in A
for num in B:
    if num in A:
        print(1)
    else:
        print(0)
