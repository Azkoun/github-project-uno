product_nums= ['V475', 'F987', 'Q143', 'R68A']

search = input('Enter a product number:')

#method 1 of checking if a number exists in the list

if search in product_nums:
    print(search, 'was found in the list!')
else:
    print(search, 'was not found in the list!')
    
#method 2 using a loop and finding 

found=False
index= -1
for i in range(len(product_nums)):
    if product_nums[i]==search:
        found = True
        break
    
if found:
    print(search, 'was found in the list!')
else:
    print(search, 'was not found in the list!')
    