filename = input("Enter file name: ")
text = input("Enter text: ")

with open(filename, "a") as file:
    file.write("\n" + text)

print("Data appended successfully")