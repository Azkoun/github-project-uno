h = int(input('Enter height of diamond: '))

for i in range(1, h+1):
    if h % 2 != 0:

        for j in range(1,h-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            print("*", end="")
        print()

for i in range(h-1,0,-1):
    if h% 2 != 0:
        for j in range(1,h-i+1):
                  print(" ", end="")
        for j in range(1, 2*i):
            print("*", end="")
        print()





  
           



    