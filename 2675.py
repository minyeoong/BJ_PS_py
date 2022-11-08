a = int(input())
for i in range(a):
    num, s = input().split()
    str =''
    for j in s:
        str+=(j*int(num))
    print(str)
    