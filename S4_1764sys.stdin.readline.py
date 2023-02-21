# N,M = map(int,input().split())
# d =[input() for _ in range(N)]
# b=[input() for _ in range(N)]
# db=[]
# for s in d:
#     if s in b:
#         db.append(s)
# db.sort()
# print(len(db))
# for i in db:
#     print(i)

# N,M = map(int,input().split())
# d =[input() for _ in range(N)]
# b=[input() for _ in range(N)]
# db = set(d)&set(b)
# db=list(db)
# db.sort()

# print(len(db))
# for i in db:
#     print(i)

#ChatGPT
import sys

n, m = map(int, sys.stdin.readline().split())

# Create sets to store names
hear = set()
see = set()

# Add names to "hear" set
for _ in range(n):
    name = sys.stdin.readline().strip()
    #input()을 이용하는 것보다 훨씬 러닝타임이 짧아진다.
    hear.add(name)
#집합의 경우 add 함수를 이용한다.


# Check if each name in "see" set is in "hear" set
result = []
for _ in range(m):
    name = sys.stdin.readline().strip()
    if name in hear:
        result.append(name)

# Sort and print the result
result.sort()
print(len(result))
for name in result:
    print(name)

