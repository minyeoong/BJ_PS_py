# len = int(input())
# divisor =list(map(int,input().split()))
# divisor.sort()
# print(divisor[0]*divisor[len-1])


N = input()
a = list(map(int, input().split()))
print(min(a)*max(a))

'''
약수를 입력하고 해당 숫자를 찾는 문제
난이도: 브1
약수의 대칭성을 이용하여 약수 중 가장 작은 수와 가장 큰 수를 곱한다.
map(int,input().split())을 이용하는 것이 핵심이었다.
https://ccamppak.tistory.com/38 
읽어보자
'''