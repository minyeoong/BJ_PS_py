# N,K = map(int,input().split())

# Series = [i for i in range(1,N+1)]*(2*N)
# yose = []
# cur = -1
# for _ in range(N):
#     for i in range(K):
#         cur+=1
#         while(Series[cur]==0):
#             cur+=1
          
#     yose.append(Series[cur])
#     for j in range(N):
#             Series[cur+j*N]=0
#     #Series[cur+j*N for j in range(K)] = 0
#     #Series[cur]=0
# yose = str(yose)[1:-1]
# print('<',end='')
# print(yose,end='')
# print('>')    
    
# N,K = map(int,input().split())

# Series = [i for i in range(1,N+1)]
# yose = []
# cur = -1
# for _ in range(N):
#     for i in range(K):
#         cur+=1
#         if cur>N-1:
#             cur-=N
#         while(Series[cur]==0):
#             cur+=1
#             if cur>N-1:
#                 cur-=N
#     yose.append(Series[cur])
#     Series[cur]=0

# yose = str(yose)[1:-1]
# print('<',end='')
# print(yose,end='')
# print('>')    
    
N,K = map(int,input().split())

Series = [str(i) for i in range(1,N+1)]
yose = "<"
cur = 0
for i in range(N):
    cur = (cur+K-1) % len(Series)
    yose += Series.pop(cur) + ", "
yose = yose[:-2] + ">"
print(yose)


