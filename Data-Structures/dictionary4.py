dictionary = {
    "name": "Suhani ",
    "age": 21,
    "city": "Bhopal"
}

print("Keys:")
for key in dictionary.keys():
    print(key)

print("\nValues:")
for value in dictionary.values():
    print(value)

print("\nKeys and Values:")
for key, value in dictionary.items():
    print(key, ":", value)