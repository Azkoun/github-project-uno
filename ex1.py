#read two sorted list and merge them into one sorted list
l1 = input().split()
l2 = input().split()
l3 = []
for i  in range(l1):
    l1[i]=int(l1[i])
for i in range(l2):
    l2[i]=int(len[i])

i = 0
j = 0
while i<len(l1)and j<len(l2):
    if l1[i]<l2[j]:
        l3.ppend(l1[i])
        i+=1
        j+=1
if len(l1)>len(l2):
    l3 = l3.append
