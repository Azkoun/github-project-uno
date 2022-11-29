s = str(input())
n = int(input())
min = 999
winner = ""
for i in range(n):
    x = str(input())
    if len(s) == len(x):
        counter = 0
        for g in range(len(s)):
            if s[g] != x[g]:
                counter = counter+1 
        
        if counter < min:
            min = counter 
            winner = x
print(winner)



