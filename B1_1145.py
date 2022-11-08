multi= list(map(int,input().split()))
multi.sort()
i= multi[0]
cnt=0
while(1):
    for j in range(5):
        if(i%multi[j]==0):
            cnt+=1
    if(cnt>=3):
        break
    cnt=0
    i+=1
print(i)