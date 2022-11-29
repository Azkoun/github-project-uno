x = int(input("enter a four digit integer number:"))
num1 = x % 10
x =  x // 10
num2 = x % 10
x = x // 10
num3 = x % 10
num4 = x // 10
print(num1 ,num2, num3, num4, sep="   ")


