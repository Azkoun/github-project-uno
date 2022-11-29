#writ a program that reads a list of integers from the user ands the second largets number(second max)
#you should not use the min,max, and sort functions or methods>
l = input().split()
for i in range(len(l)):
    l[i]= int(l[i])
#solution 3: manual algorithm
if len(l)>=2:
    if l[0]<l[1]:
        first_max=l[1]
        second_max = l[0]
    else:
        first_max=l[0]
        second_max=l[1]
    for i in range(2,len(l)):
        if l[i]>first_max:
            second_max=first_max
            first_max=l[i]
        elif l[i]>second_max:
            second_max = l[i]
    print(second_max)