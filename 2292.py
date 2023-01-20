#sol1)
n = int(input())
cnt = 1
nums_pileup = 1

while n > nums_pileup:
    nums_pileup +=cnt*6
    cnt +=1
print(cnt)

#sol2)
N = int(input())
i=0
sum =1
cnt =1
while N>sum:
    i+=6
    sum+=i
    cnt+=1
print(cnt)
'''
난이도: 브론즈2
1. 공차가 6씩 늘어나는 수열임을 이해한다.
2. while문을 이용한다.

sum의 값은 
n=1 -> 1
n=2 -> 1+6
n=3 -> 1+6+12
따라서 N값이 sum보다 클 때만 while문을 통과하여 cnt++을 진행한다.
'''
