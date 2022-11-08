n,m = map(int,input().split())
castle=[]

for _ in range(n):
    castle.append(input()) #2차원 배열을 입력받을 때 이러한 방법으로 넣기도 한다.

row = []
col = []

for i in range(n):
    row.append("X" not in castle[i])

for j in range(m):
    col.append("X" not in [castle[i][j] for i in range(n)])  #list에서 for문을 진행할 수 있다.  

print(max(sum(row),sum(col)))