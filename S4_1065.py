def HanNum(N):
    if int(N)<100:
        return 1
    if int(N)==1000:
        return 0
    else:
        a = int(N[1])-int(N[0])
        b = int(N[2])-int(N[1])
        if a==b:
            return 1
        else:
            return 0

N = input()
cnt =0
for i in range(1,int(N)+1):
    #if HanNum(i):
    if HanNum(str(i)):
        cnt+=1
print(cnt)
            
            
#by ChatGPT 
def is_hansu(n):
    if n < 100:
        # All numbers less than 100 are Han numbers.
        return True
    else:
        # For numbers greater than or equal to 100,
        # we need to check if the difference between adjacent digits is the same.
        digits = [int(x) for x in str(n)]  # Convert the number to a list of digits.
        diff = digits[1] - digits[0]  # Compute the difference between the first two digits.
        #어차피 등차수열은 공차가 상수이므로 대입시켜서 뒤는 계속 이 상수와 비교하면 된다.
        for i in range(2, len(digits)):
            if digits[i] - digits[i-1] != diff:
                return False
        return True

n = int(input())
count = 0
for i in range(1, n+1):
    if is_hansu(i):
        count += 1
print(count)
