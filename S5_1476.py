E,S,M = map(int,input().split())
N =1

while(1):
    Ey,Sy,My = N%15,N%28,N%19
    if N%15==0:
        Ey=15
    #15의 배수일 때는 15로 나눴을 때 0이 되는 문제가 발생한다.
    if N%28 ==0:
        Sy=28
    if N%19==0:
        My=19
    if Ey ==E and Sy==S and My ==M:
        print(N)
        break
    N+=1

#브루트포스 알고리즘이다.