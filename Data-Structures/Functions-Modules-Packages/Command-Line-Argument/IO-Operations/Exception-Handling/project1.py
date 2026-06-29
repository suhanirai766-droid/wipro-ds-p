import os

try:
    filename = input("Enter the file name: ") + ".txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as file:
        lines = file.readlines()

    items = 0
    free_items = 0
    amount = 0
    discount = 0

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        data = line.split()

        if data[0] == "Discount":
            discount = int(data[1])

        elif data[1] == "Free":
            free_items += 1

        else:
            items += 1
            amount += int(data[1])

    print("No of items purchased:", items)
    print("No of free items:", free_items)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", amount - discount)

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print("Error:", e)