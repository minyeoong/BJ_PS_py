def sig(k):
    return k*(k+1)//2

N = int(input())
k=1
while(1):
    if sig(k)>N:
        break
    k+=1
    
if sig(k)==N:
    print(k)
else:
    print(k-1)