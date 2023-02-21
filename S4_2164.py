from collections import deque
import sys

# Read in the value of n
n = int(sys.stdin.readline())

# Create a deque with the numbers 1 to n
cards = deque(range(1, n+1))

# Keep removing the first element and moving the second element to the end
while len(cards) > 1:
    cards.popleft()  #왼쪽에서 pop
    cards.rotate(-1) #왼쪽으로 이동

# Print the remaining element, which is the last card left
print(cards[0])
