def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

str= str(factorial(int(input())))
str =str[::-1]
cnt= 0
for i in str:
    if i =='0':
        cnt+=1
    else:
        print(cnt)
        break