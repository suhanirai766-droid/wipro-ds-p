numbers = [10, 20, 30, 40, 50]

index = int(input("Enter index to remove: "))

if 0 <= index < len(numbers):
    numbers.pop(index)
    print("Updated List:", numbers)
else:
    print("Invalid index")