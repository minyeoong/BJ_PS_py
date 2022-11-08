while(1):
    N = list(input())
    if(N[0]=="0"):
        break
    l = len(N)
    IsF=True
    for i in range(l//2):
        if(N[i]!=N[l-1-i]):
            IsF=False
            #bool을 이용해 모든 loop상황을 만족해야 true인 알고리즘을 짜려면
            #조건을 벗어나는 경우가 한번이라도 있으면 false를 만들면 된다.
            
    if(IsF == True):
        print('yes')
    else:
        print('no')
