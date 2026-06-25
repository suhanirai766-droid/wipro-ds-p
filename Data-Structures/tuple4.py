numbers = (10, 20, 30, 40, 50)

element = int(input("Enter element: "))

if element in numbers:
    print("Index:", numbers.index(element))
else:
    print("Element not found")