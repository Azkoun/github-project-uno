min = int(input("enter number of minutes"))
days = min //60//24
hours = min//60 %24
mins = (min) % 60
print(min , "minutes are" , days , "days," , hours,"hours, and", mins , "minutes"  )