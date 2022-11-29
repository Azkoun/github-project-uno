import math

num = int(input())
if num % 2 != 0:
    length = 1
else:
    length = 2
spaces = num - (num // 2)

while length <= num:
    print(' ' * spaces + 'x' * length)
    length += 2
    spaces -= 1
    