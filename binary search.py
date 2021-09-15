def binarySearch(alist,item):
if len(alist) == 0:
return False
else:
midpoint = len(alist)//2
if alist[midpoint]==item:
return True
else:
if item<alist[midpoint]:
return binarySearch(alist[:midpoint],item)
else:
return binarySearch (alist[midpoint+1:],item)
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,] print(testlist)
a=int(input("Enter the number to be searched"))
print (binarySearch(testlist, a))
