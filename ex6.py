x = int(input("enter three digit integer:"))
num1 = x % 10
x  = x//10
num2 = x % 10
x = x// 10
num3 = x%10
print(num1, num2, num3, sep=(" "))

