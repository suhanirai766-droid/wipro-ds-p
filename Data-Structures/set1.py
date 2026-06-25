numbers = {10, 20, 30, 40, 50}

item = int(input("Enter item to remove: "))

if item in numbers:
    numbers.remove(item)
    print("Updated set:", numbers)
else:
    print("Item not found")