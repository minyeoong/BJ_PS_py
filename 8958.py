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
        
    

