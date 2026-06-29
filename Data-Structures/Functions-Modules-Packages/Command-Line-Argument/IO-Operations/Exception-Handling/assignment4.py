try:
    numbers = [10, -5, 20, -15, 30, -25, 40, -35, 50, -45]

    index = int(input("Enter index: "))

    if numbers[index] >= 0:
        print("Positive Number")
    else:
        print("Negative Number")

except IndexError:
    print("Invalid Index")

except ValueError:
    print("Enter integer only")
    