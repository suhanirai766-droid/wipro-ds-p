dictionary = {
    "name": "Suhani Rai",
    "age": 21,
    "city": "Bhopal"
}

key = input("Enter key: ")

if key in dictionary:
    print("Key exists")
else:
    print("Key does not exist")