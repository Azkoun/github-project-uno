 my_num = -5
print(abs(my_num)) #absolute value
print(pow(4 , 26)) #power of 26
print(max(4 , 6)) # bigger number
print(min(5 ,8)) # smaler number 
print(round(3.7)) # rounds it up


x = 5656.8787
print(round(x))
print(format(45455.6565 , ',.2f'))

from math import *
print(floor(3.7)) #deletes whats next to .
print(ceil(4.5)) # rounds it up
print(sqrt(36)) # square root






friends = ["adrien",'elio' , "fadi " , "dani"]
friends[1] = "adrien"
print(friends[1:3])



is_male = False
is_tall = False
if is_male and is_tall:
    
    print("you are a male and you are tall")
elif is_male and not(is_tall):
    print("YOU ARE A SHORT MALE")
elif not(is_male) and (is_tall):
    print("you are a female and short")
else:
        
        print("go back to the kitchen, shortass")
        
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
     return num3
 
print(max_num(300, 40, 60))

v1 = float(input(" enter first number: "))
op = input("enter an operator:")
v2 = float(input("enter second number:"))

if op == "+":
    print(v1 + v2)
if op =="-":
    print(v1 - v2)
if op == "/":
    print(v1 / v2)
if op == "*":
    print(v1 * v2)
if op == "**":
     print(v1 ** v2)
else:
         print("syntax error")
         


         
male = False
female = False
if (male) and not (female):
    print("you are male and female")
elif (male) and not (female):
    print("you are male and not female")
elif not (male) and not (female):
    print("you do no exist, your caryotype doesn't contain X or Y chromosomes")
    
    





    
    
    
    
    

    
    
    
    
    

    



    
    
    
    
        

        
        
    






    
        
    
    







