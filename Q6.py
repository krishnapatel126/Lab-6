t = eval(input("Enter a tuple: "))
index = int(input("Enter index to modify: "))
value = input("Enter new value: ")

temp = list(t)
temp[index] = value
modified = tuple(temp)

print("Modified tuple:", modified)
