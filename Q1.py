data = eval(input("Enter the list: "))

boys = sum(1 for person in data if isinstance(person, tuple))
girls = sum(1 for person in data if not isinstance(person, tuple))

print("Number of boys:", boys)
print("Number of girls:", girls)
