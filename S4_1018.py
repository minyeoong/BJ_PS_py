#failed

n,m = map(int, input().split())
board = [input() for _ in range(n)]
check1 = ['BWBWBWBW','WBWBWBWB']*4
check2 = ['WBWBWBWB','BWBWBWBW']*4

def count_changes(x,y):
    changes1 = 0
    changes2 = 0
    for i in range(8):
        for j in range(8):
            if check1[i][j]!=board[x+i][y+j]:
                changes1 +=1
                
            if check2[i][j]!=board[x+i][y+j]:
                changes2 +=1
            
    return min(changes1,changes2)
minchange = n*m
for i in range(n-7):
    for j in range(m-7):
        minchange = min(count_changes(i,j),minchange)
        
print(minchange)

'''
8*8의 정답 판을 만들어 놓고 
이중포문을 통해 빠짐없이 x,y를 늘려가며 전체 n*m에 대해
탐색하고 최소를 찾는 방법이다.

board = [input() for _ in range(n)]
check1 = ['BWBWBWBW','WBWBWBWB']*4
check2 = ['WBWBWBWB','BWBWBWBW']*4

파이썬으로 2차원 배열을 이용하려면
위와같은 표현방법을 익혀두어야한다.
'''