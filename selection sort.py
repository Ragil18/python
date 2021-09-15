def selectionSort(alist):
for i in range(len(alist)-1,0,-1):
pos=0
for location in range(1,i+1):
if alist[location]>alist[pos]:
pos= location
temp = alist[i]
alist[i] = alist[pos]
alist[pos] = temp
alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
