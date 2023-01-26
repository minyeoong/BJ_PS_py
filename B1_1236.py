# n,m = map(int,input().split())
# castle=[]

# for _ in range(n):
#     castle.append(input()) #2차원 배열을 입력받을 때 이러한 방법으로 넣기도 한다.

# row = []
# col = []

# for i in range(n):
#     row.append("X" not in castle[i])

# for j in range(m):
#     col.append("X" not in [castle[i][j] for i in range(n)])  #list에서 for문을 진행할 수 있다.  

# print(max(sum(row),sum(col)))


row, col = map(int,input().split())
castle=[]
for _ in range(row):
    castle.append(input())
cnt_row =row 
flag=False
for i in range(row):
    for j in castle[i]:
        if "X" in j:
            flag=True
    if flag==True:
        cnt_row-=1
    flag=False
    
        
flag=False
cnt_col=col
for j in range(col):
    if "X" in [castle[i][j] for i in range(row)]:
        flag=True
    if flag ==True:
        cnt_col-=1
    flag =False
# print(cnt_row)
# print(cnt_col)
print(max(cnt_row,cnt_col))
            
