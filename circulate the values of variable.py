def rotate(l, n):
return l[n:] + l[:n]
list = [1, 2, 3, 4, 5]
print(" List:",list)
my_list=rotate(list, 1)
print("Clockwise Rotate by 1:",my_list)
my_list=rotate(list, 2)
print("Clockwise Rotate by 2:",my_list)
my_list=rotate(list, -2)
print("Anti-clockwise Rotate by 2:",my_list)
