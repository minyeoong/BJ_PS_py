N = int(input())
sum=0
line =0
while(N>sum):
    line+=1
    sum+=line
if line%2 ==1:
    #3/1
    print(1+sum-N,end='')
    print('/',end='')
    print(line-(sum-N))
else:
    print(line-(sum-N),end='')
    print('/',end='')
    print(1+sum-N)