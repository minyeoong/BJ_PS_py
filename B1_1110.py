num = int(input())
cnt=0
if (num<10):
    num*=10
store_num =num
while 1:
    cnt+=1
    num = (num%10)*10 +(num%10 + (num//10)%10)%10
    if(store_num == num):
        break
print(cnt)

# N = int(input())  #입력받은 값을 int로 바꿈
# num = N           #변하는 값
# count = 0         #몇 번 사이클인지
 
# while True:
#     a = num//10
#     b = num %10
#     c = (a+b)%10
#     num = (b*10) + c
#     count += 1
#     if(num == N):
#         break
 
# print(count)

'''
규칙을 이용해 숫자를 만든다.
난이도: 브1

한 자리 숫자냐 두 자리 숫자냐 나눈다.
while 문을 이용해 cnt를 증가시키며 store_num과 새로 만든 num을 비교한다.
'''
