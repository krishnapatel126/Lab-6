tuple_list = eval(input("Enter list of tuples: "))

cleaned_list = [t for t in tuple_list if t]

print("List after removing empty tuples:", cleaned_list)
