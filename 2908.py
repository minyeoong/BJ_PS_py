a,b = input().split()
a = int(a[::-1])
b = int(b[::-1])
if a>b:
    print(a)
else:
    print(b)
'''
난이도: 브론즈2
1. 받은 숫자를 뒤집기

a[::-1]이 핵심이었다.
뒤집는 등 변형을 가할 때는 문자열이 숫자보다 쉬우므로 문자열로 처리하고 int()로 바꿔준다.
a[::-1] is a slice notation in python which is used to reverse a string or sequence. 
The slice notation is start:stop:step, and in this case, 
the start and stop parameters are omitted which means it starts at the beginning 
and goes to the end of the string. The step parameter is set to -1,
which means to go through the string in reverse order,
so every element is accessed in reverse order.
So, a[::-1] is used to reverse the string stored in variable 'a'

ex)
a = 'abcdefg'
print(a[::-2]) //geca
'''