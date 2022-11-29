l1= input().split()
l2 = input().split()
l3 = []
for i  in range(len(l1)):
    l1[i]=int(l1[i])
for i in range(len(l2)):
    l2[i]=int(l2[i])
if len(l1)>len(l2):
    smaller = l2
    bigger= l1
else:
    bigger = l2
    smaller = l1
for i in range(len(smaller)):
    l3.append(smaller[i]-bigger[i])
for i in range(len(smaller),len(bigger)):
    l3.append(bigger[i])
print(l3)
