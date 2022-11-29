#read two lists of different size an calculate their sum in a third list.
l1 = input().split()
l2 = input().split()
l3 = []
for i in range(len(l1)):
    l1[i]=int(l1[i])
for i in range(len(l2)):
    l2[i]=int(l2[i])
if len(l1)<len(l2):
    shortest = l1
    longest = l2
else:
    shortest = l2
    longest = l1
for i in range(len(shortest)):
    l3.append(l1[i]+l2[i])
l3+= longest[len(shortest):]
print(l3)



