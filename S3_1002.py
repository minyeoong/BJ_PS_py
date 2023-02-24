def Cal_distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
def Print_pointNum(d,r1,r2):
    if d==0:
        if r1!=r2:
            print(0)
        else:
            print(-1)
    else:  
        if d>r1+r2:
            print(0)
        if d==r1+r2:
            print(1)
        if d<r1+r2:
            if d+min(r1,r2)<max(r1,r2):
                print(0)
            if d+min(r1,r2)==max(r1,r2):
                print(1)
            if d+min(r1,r2)>max(r1,r2):
                print(2)
            

N =int(input())
for _ in range(N):
    coord=list(map(int,input().split()))
    d=Cal_distance(coord[0],coord[1],coord[3],coord[4])
    r1,r2 = coord[2],coord[5]
    Print_pointNum(d,r1+r2)
    # if d==0:
    #     print(-1)
    # else:
    #     if d>r_sum:
    #         print(0)
    #     if d==r_sum:
    #         print(1)
    #     if d<r_sum:
    #         print(2)