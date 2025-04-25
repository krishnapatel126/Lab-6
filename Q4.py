n = int(input("Enter number of food items: "))
items = []

for _ in range(n):
    name = input("Enter food item: ")
    price = float(input("Enter price: "))
    items.append((name, price))

sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

print("Sorted food items by price (descending):")
for item in sorted_items:
    print(item)
