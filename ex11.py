number= input()
maxNumber=0

for i in range(len(number)):
  if number[i]=="0":increment=9
  elif number[i]=="9":increment=0
  else:increment=int(number[i]) + 1
  newNumber=number[0:i] +str(increment) + number[i+1::]
  if int(newNumber) > maxNumber:maxNumber=int(newNumber)

print(maxNumber)