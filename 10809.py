word = input()
alphabet = list(range(97,123))
for x in alphabet:
    print(word.find(chr(x)))

'''
난이도: 새싹
1. abcd.. 모든 알파벳에 대하여 알파벳 순서대로 접근한다.
2. 문자열에서 해당 알파벳이 처음으로 등장하는 인덱스를 출력한다.

find함수를 익히기 위한 문제이다.
알파벳 순서대로 접근해야 하므로 list(range(97,123))을 통해 알파벳 아스키코드 배열을 만든다.
chr(x)을 통해 알파벳으로 바꿔 주면서 str.find(chr(x))을 통해 해당 문자가 처음 등장하는 
인덱스 값을 반환해서 바로 출력한다.
문자를 찾지 못한다면 -1 을 반환한다.
str.index()함수도 비슷한 기능을 하지만 문자를 찾지 못한다면 
error를 내는 차이점이 있다.

string.find(substring, start, end)
Where:

substring is the substring to be searched for.
start and end (optional) are indices specifying the range of the string to be searched.
The default value of start is 0, and the default value of end is the length of the string.
'''