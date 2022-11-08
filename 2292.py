n = int(input())
cnt = 1
nums_pileup = 1

while n > nums_pileup:
    nums_pileup +=cnt*6
    cnt +=1
print(cnt)