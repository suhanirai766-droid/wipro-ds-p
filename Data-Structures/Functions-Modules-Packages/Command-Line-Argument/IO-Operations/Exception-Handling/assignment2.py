try:
    n = int(input("Enter a number: "))

    if n <= 1:
        print("Not Prime")
    else:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break

        if prime:
            print("Prime")
        else:
            print("Not Prime")

except ValueError:
    print("Invalid Input")