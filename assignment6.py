num = int(input("Enter a number:" \
""))

if num < 2:
    print("Not Prime")
else:
    prime = True
    for i in range(2,
int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("prime")
    else:
        print("Not Prime")
