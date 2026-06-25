text = input("Enter a string: ")
n = int(input("Enter n: "))

last = text[-n:]
result = last * n

print(result)