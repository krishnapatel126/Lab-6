t = eval(input("Enter a tuple: "))
index = int(input("Enter index to delete: "))

temp = list(t)
del temp[index]
new_tuple = tuple(temp)

print("Tuple after deletion:", new_tuple)
