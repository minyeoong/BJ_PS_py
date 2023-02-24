# arr =[-1 for _ in range(10**6+1)]
# N = int(input())
# i=1
# j=1
# cnt=0
# arr[1]=0
# while(i<N or j<N):
#     cnt+=1
#     i=2**cnt
#     j=3**cnt
#     arr[i]=cnt
#     arr[j]=cnt
# k=1
# cnt2=0
# cnt3=0
# while(k<N):
#     cnt2+=1
#     while(k<N):
#         cnt3+=1
#         k=(2**cnt2)*(3**cnt3)
#         arr[k]=cnt2+cnt3
#     k=2**cnt2
# total=0
# while(arr[N]==-1):
#     N-=1
#     total+=1
# print(total+arr[N])

'''
시도는 좋았지만 Dynamic Programming의 중요한 원리를 이용해야 한다.
ex) 10
가장 큰 수로 나누는 것이 베스트라고 생각이 된다. 
10->5->4->2->1
하지만 Optimal Solution이 아니다.
따라서 이 문제는 Greedy Algorithm이 아닌 Dynamic Programming으로 접근해야한다.
Dynamic Programming에선 Memozation을 이용해서 
이 전에 저장한 값들을 계속해서 이용하는 것이 중요하다.
'''
# Read input n
n = int(input())

# Create a list to store the minimum number of operations for each number from 1 to n
dp = [0] * (n + 1)

# Loop through all numbers from 2 to n and compute the minimum number of operations for each number
for i in range(2, n + 1):
    # Initialize the minimum number of operations to the number of operations for i-1 plus 1 (subtract 1)
    dp[i] = dp[i - 1] + 1
    # If i is divisible by 2, update the minimum number of operations for i
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # If i is divisible by 3, update the minimum number of operations for i
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

# Print the minimum number of operations for n
print(dp[n])

'''
dp = [0] * (n + 1)
이 방법을 생각하지 못했었다.
파이썬에서는 쉽게 리스트를 만드는 방법이 있는데 
같은 값을 n 크기의 리스트에 저장하고 싶으면 
[k]*n의 형태로 이용할 수 있다는 것을 잊지 말자

dp[i] = dp[i - 1] + 1
전체를 초기화 해준다. 이 또한 점화식을 이용해서 
-1식만을 사용했을 때 (가장 basic방식)의 solution을 할당한다.

그 후에 추가적인 조건 /2,/3을 이용한다.
이 역시 
if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
와 같이 min()함수를 통해 원래 기록된 basic방식과 비교하면서 할당해준다.

'''

    