#sol1)
a = int (input())
for i in range(a):
    oxList = list(input())
    score = 0
    sumScore = 0
    for j in oxList:
        if j=='O':
            score+=1
            sumScore +=score
        else:
            score = 0
    print(sumScore)

#sol2)
N = int(input())
for _ in range(N):
    str = input()
    cnt =0
    sum =0
    for i in str:
        if i=='X':
            cnt=0
        else:  #X가 아닌 경우에 밑의 code를 진행시키면 안되므로 else를 써야만 한다.
            cnt+=1
            sum+=cnt
    print(sum)

'''
OX문자열을 받아서 점수를 체크하는 문제
난이도: 브론즈2

1. X받으면 초기화
2. X받기 전까진 공차1인 등차수열

'X'를 받으면 cnt=0으로 초기화 시키고 
그렇지 않다면 문자열 전체 길이에 대해서 cnt+=1, sum+=cnt를 진행한다.
'''