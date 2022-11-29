import random
response_size = 40
frequency_size = 11
response = [0]*response_size
frequency = [0]*frequency_size
for i in range(response_size):
    print("enter response #", i+1, sep=": ")
    response[i]=int(input())
    while response[i]<1 or response[i]>10:
        print("error:invalid response value!")
        print("enter response #",i+1,sep = "",end = ":")
        response[i]= int(input())
for i in range(response_size):
    frequency[response[i]]+=1
print()
print("rating", format("frequency",">17s"))
for rating in range(1,frequency_size):
    print(format(rating,"6d"),format(frequency[rating], "17d"))
        