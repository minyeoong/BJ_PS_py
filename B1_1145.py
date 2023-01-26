# multi= list(map(int,input().split()))
# multi.sort()
# i= multi[0]
# cnt=0
# while(1):
#     for j in range(5):
#         if(i%multi[j]==0):
#             cnt+=1
#     if(cnt>=3):
#         break
#     cnt=0
#     i+=1
# print(i)

a = list(map(int,input().split()))
for i in range(min(a)*2,a[len(a)-1]*a[len(a)-2]*a[len(a)-3]+1):
    cnt=0
    for j in a:
        if i % j ==0:
            cnt+=1
    if cnt>=3:
        print(i)
        break  

'''
난이도:브1 
브루트포스 문제라 방법은 다양할 것이다.
모든 요소를 나눴을 때 3개 이상 나머지가 0일 때 break를 걸어준다.
'''