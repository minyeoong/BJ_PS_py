a = int(input())
for i in range(a):
    num, s = input().split()
    str =''
    for j in s:
        str+=(j*int(num))
    print(str)

'''
난이도: 브론즈2
1.문자열에서 원하는 횟수만큼 알파벳 반복 출력
2.각 인덱스마다마다 진행해야함

str =''
for j in s:
    str+=(j*int(num))
    
핵심 코드이다. str=''을 통해 빈 문자열을 만들어 주고 빈 문자열에
각 문자를 반복 횟수만큼 붙여 넣어주는str+=(j*int(num))방식이다.
'''

N = int(input())
for _ in range(N):
    Num,str = input().split()
    for i in str:
        #for _ in range((Num-'0')): 파이썬에서는 아스키코드 변환할 때 ord(),chr()함수를 이용한다.
        for _ in range(int(Num)):
            print(i, end='')
    print('')
        
'''
sol2)
1.문자열에서 원하는 횟수만큼 알파벳 반복 출력
2.각 인덱스마다마다 진행해야함

split()함수를 통해 한 줄에 반복 횟수와 문자열을 입력 받는다. 각 문자에 대해 
반복 횟수만큼 반복 출력한다.
파이썬에서는 print할 때 자동으로 개행이 진행된다.
default값으로 end='\n'가 포함 돼 있기 때문이다. 
따라서  print(i,end='')을 이용하면 개행 없이 출력이 가능하다.
'''
