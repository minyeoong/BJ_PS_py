#중복된 숫자의 개수가 가장 많은 만큼
#6이나 9의 경우에는 합쳐서 계산

str = input()
str = str.replace('6','9')
set_str = set(str)
max=0

for i in set_str:
    if i=='9':
        count = (str.count(i)+1)/2 #999의 경우 2출력
    else:
        count = str.count(i)
        
    if max<count:
        max =count
print(int(max))
    
    
'''
6,9를 완전히 동일한 것으로 볼 수 있는 것이 핵심이었다.
이를 처리하는 방법으로
 str = str.replace('6','9')를 통해 
 모든 6을 9로 바꾸면서 9일 떄 +1/2 조건을 추가했다.
'''