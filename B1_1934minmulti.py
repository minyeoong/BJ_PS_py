T= int(input())
for _ in range(T):
    N,M = map(int, input().split())
    store_M =M
    N_divisior=[]
    M_divisior=[]
    i=2
    while(N>1):
        while(N%i==0):
            N_divisior.append(i)
            N=N//i
        
        i+=1
    i=2
    while(M>1):
        while(M%i==0):
            M_divisior.append(i)
            M=M//i
        i+=1
    result=1
    for j in N_divisior:
        if(store_M%j==0):
            store_M =store_M//j
        result*=j 
    
    result*=store_M
    print(result)
        
            